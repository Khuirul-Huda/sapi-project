<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="container mx-auto mt-5 flex items-center gap-5 text-white mb-20 outfit-400">
    <h1 class="outfit-800 text-white text-3xl ml-7">SAPI</h1>

    <nav class="flex md:gap-14 gap-3 justify-center w-full">
      <RouterLink to="/">Products</RouterLink>
      <RouterLink to="/">Community</RouterLink>
      <RouterLink to="/about">Blog</RouterLink>
      <RouterLink to="/about">Contact</RouterLink>
    </nav>
  </header>

  <RouterView />

  <footer class="mt-10">
    <p class="outfit-300 text-sm mt-5 md:text-lg text-center text-white">
      Copyright &copy; 2023.<br />
      Huda, Sheva, Zuhail, Mahendra, Rizwah
    </p>
  </footer>
</template>
