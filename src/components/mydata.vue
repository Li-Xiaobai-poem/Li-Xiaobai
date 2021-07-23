<-编辑信息-->

<template>
  <div id="mydata">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-header style=" background-color: rgba(84,92,100,0.5);
    color: #333;
    text-align: center;
    line-height: 60px;">
        <el-row>
          <el-col :span="2" :offset="11">
            <div>编辑信息</div>
          </el-col>
          <el-col :span="2" :offset="9">
            <router-link to='/myhome'>
              <el-button size="small" style="background-color: unset;color:#000000">返回</el-button>
            </router-link>
          </el-col>
        </el-row>
      </el-header>

      <el-main>
        <el-row>
          <el-col :span="10" :offset="6">
            <el-form ref="form" :rules="rules" :model="changeForm" label-width="100px">
              <el-form-item label="密码" prop="password">
                <el-input v-model="changeForm.password" :type="pwdType"
                          style="background-color: rgba(246, 246, 246, 0.5)">
                  <i slot="suffix" class="el-icon-view" @click="showPwd"></i>
                </el-input>
              </el-form-item>
              <el-form-item label="确认密码" prop="repassword">
                <el-input v-model="changeForm.repassword" :type="pwdType">
                  <i slot="suffix" class="el-icon-view" @click="showPwd"></i>
                </el-input>
              </el-form-item>
              <el-form-item label="性别" prop="sex">
                <el-select :placeholder=this.sex_data v-model="changeForm.sex">
                  <el-option label="男" :value="0"></el-option>
                  <el-option label="女" :value="1"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="邮箱">
                <el-input v-model="changeForm.email" :placeholder=email></el-input>
              </el-form-item>
              <el-form-item label="城市">
                <el-input v-model="changeForm.city" :placeholder=city></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" style="background-color: rgba(246, 246, 246, 0.7);color:#000000;"
                           @click="onSubmit">提交
                </el-button>
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
      </el-main>

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
      response: '',
      pwdType: '',
      changeForm: {
        password: '',
        repassword: '',
        sex: '',
        email: '',
        city: ''
      },
      rules: {
        password: [
          {required: true, message: '密码不能为空', trigger: 'blur'},
          {min: 6, max: 50, message: '密码6-50位', trigger: 'blur'}
        ],
        repassword: [
          {required: true, message: '请再次输入密码', trigger: 'blur'}
        ]
      },
      username: this.COMMON.USERNAME,
      password: '',
      sex: '',
      email: '',
      city: 'hubei',
      sex_data: ''
    }
  },
  mounted: function () {
    this.COMMON.get_baseinformation(this, this.username)
    this.showPwd()
  },
  methods: {
    showPwd() {
      this.pwdType === 'password' ? this.pwdType = '' : this.pwdType = 'password'
      let e = document.getElementsByClassName('el-icon-view')[0]
      this.pwdType === '' ? e.setAttribute('style', 'color: #409EFF') : e.setAttribute('style', 'color: #c0c4cc')
    },
    onSubmit() {
      console.log('submit!')
      this.change_baseinformation()
    },
    change_baseinformation() {
      if (this.changeForm.password === '' || this.changeForm.repassword === '' || this.changeForm.sex === '' || this.changeForm.email === '' || this.changeForm.city === '') {
        this.$alert('不能有信息为空', '提示', {
          confirmButtonText: '确定',
          callback: action => {
          }
        })
      } else {
        if (this.changeForm.password !== this.changeForm.repassword) {
          this.$alert('两次输入密码不同', '提示', {
            confirmButtonText: '确定',
            callback: action => {
            }
          })
        } else {
          this.$http.get('http://120.79.64.45:5000/app1/userchange', {
            params:
              {
                username: this.username,
                password: this.changeForm.password,
                sex: this.changeForm.sex,
                email: this.changeForm.email,
                city: this.changeForm.city
              }
          })
            .then((response) => {
              console.log('true')
              let res = JSON.parse(response.bodyText)
              this.response = res
              if (res.error_num === 0) {
                this.change_true()
              } else {
                this.change_false()
              }
            })
        }
      }
    },
    change_false() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: action => {

        }
      })
    },
    change_true() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: () => {
          this.$router.push({path: '/myhome'})
        }
      })
    }
  }
}
</script>
<style scoped>
#mydata {
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
</style>
!-
