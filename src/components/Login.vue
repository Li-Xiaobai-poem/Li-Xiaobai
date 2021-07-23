<template>
  <div id="login-container">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-form ref="form" :rules="rules" :model="form" label-width="80px" class="login-form"
               style="background-color: rgba(255,255,255,0.7)">
        <h2 class="login-title">登录</h2>
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="form.password" :type="pwdType" placeholder="请输入密码">
            <i slot="suffix" class="el-icon-view" @click="showPwd"></i>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" style="background-color: unset;color:#000000" @click="submitForm">登录</el-button>
          <el-button type="primary" style="background-color: unset;color:#000000" @click="registForm">注册</el-button>
        </el-form-item>
      </el-form>
    </el-container>
  </div>
</template>

<script>
import AppHeader from './AppHeader'
import AppNavbar from './AppNavbar'

export default {
  components: {AppHeader, AppNavbar},
  data() {
    return {
      pwdType: '',
      response: '',
      form: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          {required: true, message: '用户名不能为空', trigger: 'blur'},
          {min: 1, max: 1000, message: '用户名至少一位', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不能为空', trigger: 'blur'},
          {min: 6, max: 50, message: '密码6-50位', trigger: 'blur'}
        ]
      }
    }
  },
  mounted() {
    this.showPwd()
  },
  methods: {
    showPwd() {
      this.pwdType === 'password' ? this.pwdType = '' : this.pwdType = 'password'
      let e = document.getElementsByClassName('el-icon-view')[0]
      this.pwdType === '' ? e.setAttribute('style', 'color: #409EFF') : e.setAttribute('style', 'color: #c0c4cc')
    },
    submitForm: function () {
      this.$http.get('http://120.79.64.45:5000/app1/login', {
        params:
          {username: this.form.username, password: this.form.password}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.response = res
          if (res.error_num === 0) { /* 登陆成功 */ /* 加入跳转页面 */
            console.log(res['msg'])
            this.login_true()
          } else { /* 登陆失败 */
            console.log(res['msg'])
            this.login_false()
          }
        })
    },
    login_true() {
      this.COMMON.USERNAME = this.form.username
      this.$router.push({path: '/myhome'})
    },
    login_false() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: action => {

        }
      })
    },
    registForm() {
      this.$router.push({path: '/Register'})
    }
  }
}
</script>

<style acoped>
.login-form {
  width: 350px;
  margin: 160px auto; /* 上下间距160px，左右自动居中*/
  background-color: rgb(255, 255, 255); /* 透明背景色 */
  padding: 30px;
  border-radius: 20px; /* 圆角 */
}

/* 背景 */
#login-container {
  background-image: url('../assets/p5.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
  /*background: url("../assets/logo.png");*/
}

/* 标题 */
.login-title {
  color: #303133;
  text-align: center;
}

.el-header {
  /*padding-top: 20px;*/
  /*font-size: 14px;*/
  /*color: #929292;*/
  /*box-shadow: inset 0 -2px 0 0 rgba(0, 0, 0, 0.07);*/
  /*padding-bottom: 16px;*/
  position: relative;
  width: 100%;
}

.el-main {
  position: absolute;
  left: 0px;
  right: 0px;
  top: 100px;
  bottom: 0;
  overflow-y: scroll;

}

.main {

  position: absolute;
  top: 50px;
  left: 230px;
  bottom: 0px;
  right: 0px; /* 距离右边0像素 */
  padding: 0px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  /* background-color: red; */

}

.navbar {
  position: absolute;
  width: 230px;
  top: 50px; /* 距离上面50像素 */
  left: 0px;
  bottom: 0px;
  overflow-y: auto; /* 当内容过多时y轴出现滚动条 */
  background-color: #545c64;
}

.header {
  position: absolute;
  line-height: 50px;
  top: 0px;
  left: 0px;
  right: 0px;
  background-color: #2d3a4b;
}
</style> -->
