import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import ProjectHeader from './components/ProjectHeader.vue'
import ProjectNav from './components/ProjectNav.vue'
import ProjectsIndex from './components/ProjectsIndex.vue'
import ArchitectureMap from './components/ArchitectureMap.vue'
import HomeHero from './components/HomeHero.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('ProjectHeader', ProjectHeader)
    app.component('ProjectNav', ProjectNav)
    app.component('ProjectsIndex', ProjectsIndex)
    app.component('ArchitectureMap', ArchitectureMap)
    app.component('HomeHero', HomeHero)
  },
} satisfies Theme
