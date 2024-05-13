<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header class=" container mx-auto mt-5 flex items-center  gap-5 text-white mb-20 outfit-400">
    <h1 class="outfit-800 text-white text-3xl">SAPI</h1>
   
      <nav class="flex gap-14 justify-center w-full ">
        <RouterLink to="/">Products</RouterLink>
        <RouterLink to="/">Community</RouterLink>
        <RouterLink to="/about">Blog</RouterLink>
        <RouterLink to="/about">Contact</RouterLink>
      </nav>
  
  </header>

  <RouterView />
</template>


