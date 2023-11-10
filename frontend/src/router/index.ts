import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "",
    name: "index",
    redirect: { name: "reports" },
  },
  {
    path: "/reports",
    name: "reports",
    component: () => import("../views/ReportListView.vue"),
  },
  {
    path: "/reports/:pk",
    name: "report-detail",
    component: () => import("../views/ReportDetailView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () => import("../views/NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
