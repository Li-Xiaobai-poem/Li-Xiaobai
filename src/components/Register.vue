<template>
  <div id="regist-container">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-form ref="form" :rules="rules" :model="form" label-width="80px" class="login-form"
               style="background-color:rgba(255,255,255,0.7);">
        <h2 class="regist-title">注册</h2>
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="form.password" :type="pwdType">
            <i slot="suffix" class="el-icon-view" @click="showPwd"></i>
          </el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="repassword">
          <el-input v-model="form.repassword" :type="pwdType">
            <i slot="suffix" class="el-icon-view" @click="showPwd"></i>
          </el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-select placeholder="" v-model="form.sex">
            <el-option label="男" :value="0"></el-option>
            <el-option label="女" :value="1"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="城市" prop="city">
          <el-input v-model="form.city"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" style="background-color: unset;color:#000000" @click="submitForm">注册</el-button>
        </el-form-item>
      </el-form>
    </el-container>
  </div>
</template>

<style>

</style>

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
        password: '',
        repassword: '',
        email: '',
        sex: '',
        city: ''
      },
      rules: {
        username: [
          {required: true, message: '用户名不能为空', trigger: 'blur'},
          {min: 1, max: 1000, message: '用户名至少一位', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不能为空', trigger: 'blur'},
          {min: 6, max: 50, message: '密码6-50位', trigger: 'blur'}
        ],
        repassword: [
          {required: true, message: '请再次输入密码', trigger: 'blur'}
        ],
        email: [
          {required: true, message: '请输入邮箱', trigger: 'blur'}
        ],
        city: [
          {required: true, message: '请输入城市', trigger: 'blur'}
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
    submitForm() {
      if (this.form.password === this.form.repassword) {
        this.regist()
      } else {
        this.password_false()
      }
    },
    password_false() {
      this.$alert('两次密码不一致', '提示', {
        confirmButtonText: '确定',
        callback: action => {

        }
      })
    },
    open_true() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: () => {
          this.login()
        }
      })
    },
    open_false() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: action => {

        }
      })
    },
    regist: function () {
      this.$http.get('http://120.79.64.45:5000/app1/regist', {
        params: {
          username: this.form.username,
          password: this.form.password,
          email: this.form.email,
          sex: this.form.sex,
          city: this.form.city
        }
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.response = res
          if (res.error_num === 0) { /* 注册成功，弹出小窗提示，点击后返回登陆界面 */
            this.open_true()
            console.log('注册成功')
          } else { /* 注册失败，弹出小窗提示，返回失败信息 */
            this.open_false()
            console.log('注册失败')
          }
        })
    },
    login() {
      this.$router.push({path: '/Login'})
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
.login-container {
  position: absolute;
  width: 100%;
  height: 100%;
  /*background: url("../assets/logo.png");*/
}

/* 标题 */
.login-title {
  color: #303133;
  text-align: center;
}

#regist-container {
 background-image: url('../assets/p4.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
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
  top: 60px;
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
