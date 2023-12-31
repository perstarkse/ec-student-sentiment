<template>
  <section data-scroll-section>
    <div class="container">
      <h1>Finished</h1>
      <p>
        Thank you for taking the time to look at my project. I hope you enjoyed
        it. If you have any questions or feedback, please feel free to contact
        me.
      </p>
      <div class="socials">
        <div v-for="social in socials" :key="social.text">
          <a :href="social.link">
            <h4>{{ social.text }}</h4>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: "FinishedView",
  props: {
    socials: Array,
  },
};
</script>
<style lang="scss" scoped>
section {
  padding-bottom: 15rem;
  display: grid;
  place-items: center;
  .container {
    background-color: #f5ebe0;
    padding-top: 10rem;
    padding-bottom: 20rem;
    width: 100%;
    position: relative;
    max-width: 1920px;
    padding-left: 5rem;
    padding-right: 5rem;
    text-align: center;

    img {
      position: absolute;
      top: 50px;
      right: -50px;
      height: 250px;
    }
    h1 {
      font-family: "newakeFont";
      font-size: 3rem;
      margin-bottom: 2rem;
      color: #940094;
    }
    p {
      margin-bottom: 2rem;
      font-family: "sans-serif";
    }
    .socials {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: row;
      gap: 1rem;
      a {
        color: black;
        text-decoration: none;
        font-family: "newakeFont", sans-serif; // Replace 'YourFont' with your actual font family
        display: flex;
        align-items: center;
        &:hover {
          color: #6c6c6c;
        }
        i {
          margin-right: 0.5rem; // Adds spacing between the icon and text
          font-size: 1.5rem; // Icon size, adjust as needed
          color: black;
        }
        h4 {
          font-size: 1rem; // Adjust the font size as needed
        }
      }
    }
  }
}
</style>
