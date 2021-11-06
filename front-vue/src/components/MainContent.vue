<template>
  <div class="grid">
    <main>
      <textarea
        class="textarea is-primary"
        name=""
        id=""
        cols="100"
        rows="20"
        placeholder="抽出したい記事を入力してください"
        v-model="state.text"
      ></textarea>
      <button class="button is-primary" @click="getCorpus">送信</button>
    </main>
    <aside class="sidebar-right">
      <div id="topic-box">
        <div class="card">
          <div class="card-content">
            <h3>トピックキーワード：</h3>
            <ul>
              <li
                v-for="(word, index) in state.result.topic"
                :key="index + word"
                class="tag is-primary is-light"
                style="margin: 0 2px;"
              >
                {{ word }}
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div id="summary-box">
        <div class="card">
          <div class="card-content">
            <h3>要約文：</h3>
            <div class="content">
              {{ state.result.summary }}
            </div>
          </div>
        </div>
      </div>
    </aside>
  </div>
</template>

<script>
import { reactive, defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  setup() {
    const state = reactive({
      result: [],
      text: "",
    });

    const getCorpus = async () => {
      state.result = await axios
        .get(`http://localhost/api/lda?text=${state.text}`)
        .then((res) => {
          
          return res.data;
        });
    };

    return { state, getCorpus };
  },
});
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: auto 350px;
  /* grid-template-rows: repeat(2, 100px); */
  grid-gap: 1em;
}

aside,
main {
  padding: 1em;
}

/* Demo Specific Styles */
body {
  margin: 0 auto;
  max-width: 56em;
  padding: 1em 0;
}

aside {
  padding-left: 0;
}

.card-content h3 {
  margin-bottom: 10px;
}

.card-content .content {
  font-size: 12px;
}
</style>