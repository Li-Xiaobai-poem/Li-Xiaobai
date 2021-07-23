<!--个人中心主页面-->

<template>
  <div id="myhome">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main" style="margin-top: 0">

      <el-container>
        <el-header style="font-size: 20px;
    height:100px;
    background-color: rgba(84,92,100,0.5);
    color: #333;
    text-align: center;line-height: 5px;">
          <el-row :gutter="18">
            <el-col :span="7">
              <p>用户名：{{ username }}</p>
            </el-col>
            <el-col :span="7">
              <p>性别：{{ sex_data }}</p>
            </el-col>
            <el-col :span="7">
              <el-button size="small" @click="skip_mydata" style="margin: 8px;background-color: unset;color:#000000">
                编辑个人信息
              </el-button>
            </el-col>
          </el-row>
          <el-row :gutter="18">
            <el-col :span="7">
              <p>邮箱：{{ email }}</p>
            </el-col>
            <el-col :span="7">
              <p>城市：{{ city }}</p>
            </el-col>
            <el-col :span="7">
              <el-button size="small" style="margin: 8px;background-color: unset;color:#000000"
                         @click="skip_mycollection">我的收藏
              </el-button>
            </el-col>
          </el-row>
        </el-header>

        <el-main>
          <el-col :span="24">
            <div v-for="(item,index) in this.release_poemData" :key="index">
              <el-col :span="12">
                <el-card class="box-card">
                  <div slot="header" style="height: 40px">
                    <el-row style="display: flex; justify-content: center;">
                      <el-col>{{ item.fields.keyword }}</el-col>
                    </el-row>
                    <el-row style="float: right">
                      <el-col :span="5">
                        <el-button size="mini" style="background-color: rgba(246, 246, 246, 0.7);color:#000000"
                                   @click="poem_data(item.pk)">作品详情
                        </el-button>
                      </el-col>
                    </el-row>
                  </div>
                  <el-row style="display: flex; justify-content: center;">
                    <el-col style="white-space: pre-wrap">{{ item.fields.poecontent }}</el-col>
                  </el-row>
                </el-card>
              </el-col>
            </div>
          </el-col>
        </el-main>
        <el-footer>

        </el-footer>
      </el-container>
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
      username: this.COMMON.USERNAME,
      password: '',
      email: '',
      sex: '',
      city: '',
      keyword: '',
      poecontent: '',
      sex_data: '',
      pk: '',
      release_poemData: []
    }
  },
  created: function () {
    this.show_mydata()
  },
  methods: {
    show_mydata() {
      this.COMMON.get_baseinformation(this, this.username)
      this.get_releaseinformation()
    },
    get_releaseinformation() {
      this.$http.get('http://120.79.64.45:5000/app1/releaseinfo', {
        params:
          {username: this.username}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.release_poemData = res['list']
        })
    },
    skip_mydata() {
      this.$router.push({path: '/mydata'})
    },
    skip_mycollection() {
      this.$router.push({path: '/mycollection'})
    },
    poem_data(pk) {
      this.$router.push({
        path: '/poetrydata',
        query: {
          release_id: pk
        }
      })
    }
  }
}
</script>
<style scoped>
#myhome {
   background-image: url('../assets/p3.jpg');
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

.box-card {
  margin-left: 20px;
  margin-bottom: 20px;
  width: 500px;
  height: 300px;
  background-color: rgba(246, 246, 246, 0.5);
}
</style>
