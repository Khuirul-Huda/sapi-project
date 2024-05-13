<script setup>

</script>

<template>
  <main class="container mx-auto text-white outfit-800 text-5xl ">
    <h1 class="text-center">Finds And Keeps Track of Phising</h1>
    <h1 class="text-center">And Scam Websites</h1>
    <div class="flex flex-wrap justify-center">
      <div class="flex w-1/2 flex-col justify-center">
        <h1 class="subcolor-one outfit-500 text-3xl">URL Scanner</h1>
        <form @submit.prevent="submit" class="flex gap-2">
          <input v-model="url" type="text" class=" text-2xl text-black rounded-lg outfit-300 " name="url" id="url">
          <input class="cursor-pointer text-lg p-3 bg-subcolor-two rounded-lg outfit-500" type="submit" value="SCAN">
        </form>
        <p class="outfit-300 text-lg">You can use SAPI to watch for typosquat and lookalike vaariations of a domain and scan dubiouse URLs</p>

      </div>
      <img src="/src/assets/Other 19.png" width="400px" alt="gambar">
    </div>
  </main>
</template>

<script>
export default {
  methods: {
    async submit() {
      const urlToCheck = url.value
      let formData = new FormData();
formData.append('url', urlToCheck);
      const BASE_URL = 'https://sapi-backend.mocci.my.id'
      fetch(BASE_URL + '/predict' , {body: formData, method: 'POST'}).then((res) => res.json().then((res) => {
        if (res.predict == 'good') {
          alert(res.url + ' diprediksi bukan phishing')
        } else {
          alert(res.url + ' diprediksi adalah phishing')
        }
      }))

    }
  }
}
</script>
