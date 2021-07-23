import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Products from '@/components/Products'
import Products2 from '@/components/Products2'
import Products3 from '@/components/Products3'

import Register from "@/components/Register"
import Realease from "@/components/Realease"

import Login from "@/components/Login"

import LunTan from "@/components/LunTan";
import commentDetail from "@/components/commentDetail";
import myhome from '@/components/myhome'
import mydata from '@/components/mydata'
import mycollection from '@/components/mycollection'
import poetrydata from '@/components/poetrydata'
import Publisher from "@/components/Publisher";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: '/Products',
      name: 'Products',
      component: Products
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },

    {
      path: '/LunTan',
      name: 'LunTan',
      component: LunTan
    },

    {
      path: '/commentDetail',
      name: 'commentDetail',
      component:commentDetail
    },
    {
        path: '/Products2',
      name: 'Products2',
      component:Products2
    },
    {      path: '/Products3',
      name: 'Products3',
      component:Products3

    },{
       path: '/myhome',
       name: '/myhome',
      component: myhome


    },
    {
      path: '/mydata',
      name: '/mydata',
      component: mydata
    },
    {
      path: '/mycollection',
      name: '/mycollection',
      component: mycollection
    },
    {
      path: '/poetrydata',
      name: '/poetrydata',
      component: poetrydata
    },
      {
      path: '/Publisher',
      name: '/Publisher',
      component:Publisher
    }
  ]
})
