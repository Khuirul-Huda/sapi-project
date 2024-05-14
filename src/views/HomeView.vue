<script setup></script>

<template>
  <main class="container mx-auto text-white outfit-800">
    <h1 class="text-center text-3xl md:text-5xl">Finds And Keeps Track of Phising</h1>
    <h1 class="text-center text-3xl md:text-5xl">And Scam Websites</h1>
    <div class="flex flex-wrap justify-center">
      <div class="flex md:w-1/2 flex-col items-center md:items-start justify-center">
        <h1 class="subcolor-one outfit-500 text-xl md:text-3xl mt-10 my-5">URL Scanner</h1>
        <form @submit.prevent="submit" class="flex gap-2">
          <input
            v-model="url"
            type="text"
            class="text-2xl text-black rounded-lg outfit-300"
            name="url"
            id="url"
          />
          <input
            class="cursor-pointer text-lg p-3 bg-subcolor-two rounded-lg outfit-500"
            type="submit"
            value="SCAN"
          />
        </form>
        <p class="outfit-300 text-sm w-3/4 md:w-full mt-5 md:text-lg">
          You can use SAPI to watch for typosquat and lookalike vaariations of a domain and scan
          dubiouse URLs
        </p>
      </div>
      <img src="/src/assets/Other 19.png" text-3xl md:text-5xl alt="gambar" />
    </div>

    <section id="intro" class="mx-auto">
      <h1 class="text-center text-xl md:text-3xl">What is SAPI?</h1>
      <p class="outfit-300 text-sm mt-5 md:text-lg text-center">
        SAPI stands for Say No To Phish is an application to predict phishing site. It uses Machine
        Learning Algoritm.
      </p>
    </section>
  </main>
</template>

<script>
import Swal from 'sweetalert2'

const showPhishAlert = (url) => {
  Swal.fire({
    title: 'Phishing',
    text: url + ' diprediksi sebagai situs phising!',
    icon: 'error'
  })
}

const showSafeAlert = (url) => {
  Swal.fire({
    title: 'Aman',
    text: url + ' diprediksi BUKAN situs phising',
    icon: 'success'
  })
}

export default {
  methods: {
    async submit() {
      const urlToCheck = url.value
      let formData = new FormData()
      formData.append('url', urlToCheck)
      const BASE_URL = 'https://sapi-backend.mocci.my.id'
      fetch(BASE_URL + '/predict', { body: formData, method: 'POST' }).then((res) =>
        res.json().then((res) => {
          if (res.predict == 'good') {
            showSafeAlert(res.url)
          } else {
            showPhishAlert(res.url)
          }
        })
      )
    }
  }
}
</script>
