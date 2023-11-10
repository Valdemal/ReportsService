<template>
  <section class="wrapper">
    <header>
      <ul class="nav nav-underline">
        <li class="nav-item">
          <router-link
            :to="{ name: 'reports' }"
            class="nav-link active"
            aria-current="page"
            href="#"
            >Отчеты
          </router-link>
        </li>
      </ul>
    </header>
    <main class="mt-2">
      <router-view />
    </main>
  </section>
</template>
<style>
a {
  text-decoration: none;
  color: black;
}

.wrapper {
  margin: 10px;
}
</style>
<script setup lang="ts"></script>
