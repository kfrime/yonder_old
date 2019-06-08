<template>
  <div>
    <Form ref="formData" :model="formData" :rules="validRules">
      <FormItem label="title" prop="title">
        <Input v-model="formData.title" placeholder="Enter a title"></Input>
      </FormItem>
      <FormItem label="category" prop="cate">
        <Select v-model="formData.cate" placeholder="select a category">
          <Option
            v-for="cate in cates"
            :value="cate.ID + ''"
            :key="cate.ID"
          >
            {{cate.Name}}
          </Option>
        </Select>
      </FormItem>
      <FormItem prop="content">
        <!--<Input type="textarea" v-model="formData.content" placeholder="content"></Input>-->
        <md-editer v-model="formData.content"></md-editer>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="saveArticle('formData')">Submit</Button>
      </FormItem>
    </Form>

    <p>user: {{user}}</p>
    <p>article: {{article}}</p>
    <p>cates: {{cates}}</p>
  </div>
</template>

<script>
  import MarkdownEditer from '~/components/markdown'

  export default {
    props: [
      "user",
      "article",
      "cates",
    ],
    data () {
      return {
        formData: {
          title: (this.article && this.article.Title) || '',
          cate: (this.article && this.article.Category.Id) || '',
          content: (this.article && this.article.Content) || '',
        },
        validRules: {
          title: [
            { required: true, type:"string", trigger: "blur"},
          ],
          cate: [
            { required: true },
          ],
          content: [
            { required: true, type:"string", trigger: "blur"},
          ]
        }
      }
    },
    methods: {
      saveArticle (name) {
        console.log("name:", name)
        console.log("formData:", this.formData)
        let self = this
        this.$refs[name].validate((valid) => {
          if (!valid) {
            this.$Message.error('input error');
            console.log("input not valid:", this.formData)
            return
          }
        })
      },
    },
    components: {
      "md-editer": MarkdownEditer,
    }
    // middleware: "loginRequired",
  }
</script>