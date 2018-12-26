<template>
  <div class="archive">
    <p>{{archive.year}} - {{archive.total}}</p>
    <p>{{archive.articles}}</p>
  </div>
</template>

<script>
export default {
  props: ['archive']
}
</script>