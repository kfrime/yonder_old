<template>
  <div class="markdown-wrapper">
    <textarea ref="editor"></textarea>
  </div>
</template>

<script>
  import Simplemde from 'simplemde'
  import 'simplemde/dist/simplemde.min.css'

  export default {
    name: "MarkdownEditor",
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
        indentWithTabs: false,
        lineWrapping: false,
        tabSize: 4,
      }))

      this.addEvents()
      let content = this.value ? this.value : localStorage.mdContent
      if (content) {
        this.editor.value(content)
      }
    }
  }
</script>

<style lang="less">
  .markdown-wrapper{
    font-size: 1rem;
    /*line-height: 1.2rem;*/
    line-height: 150%;

    .CodeMirror {
      height: 500px;
    }

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
