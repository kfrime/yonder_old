// vuex getters

export default {
  text (state) {
    return `${state.article.author}, ${state.article.ctime}, ${state.article.title}`
  }
}
