<template>
  <div>
    <textarea ref="editor"></textarea>
  </div>
</template>

<script>
  import Simplemde from 'simplemde'
  import 'simplemde/dist/simplemde.min.css'

  export default {
    name: "MarkdownEditer",
    props: {
      value: {
        type: String,
        default: ''
      },
      options: {
        type: Object,
        default: () => {
          return {}
        }
      },
      localCache: {
        type: Boolean,
        default: true,
      }
    },
    data () {
      return {
        editor: null,
      }
    },
    methods: {
      addEvents () {
        this.editor.codemirror.on("change", () => {
          let value = this.editor.value()
          if (this.localCache) {
            localStorage.mdContent = value
          }
          this.$emit('input', value)
          this.$emit('on-change', value)
        })
        this.editor.codemirror.on("focus", () => {
          this.$emit("on-focus", this.editor.value())
        })
      }
    },
    mounted () {
      this.editor = new Simplemde(Object.assign(this.options, {
        element: this.$refs.editor,
      }))

      this.addEvents()
      let content = localStorage.mdContent
      if (content) {
        this.editor.value(content)
      }
    }
  }
</script>

<style lang="less">
  .markdown-wrapper{
    .editor-toolbar.fullscreen{
      z-index: 9999;
    }
    .CodeMirror-fullscreen{
      z-index: 9999;
    }
    .CodeMirror-fullscreen ~ .editor-preview-side{
      z-index: 9999;
    }
  }
</style>
