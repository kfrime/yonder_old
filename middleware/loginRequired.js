export default (ctx, next) => {
  if (!ctx.$store.state.user) {
    ctx.redirect("/signin")
  }
  next()
}
