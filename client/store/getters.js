// vuex getters

export default {
  blog (state) {
    return `${state.author}, ${state.content}`
  }
}
