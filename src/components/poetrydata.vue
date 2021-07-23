<!--作品详情-->
<template>
  <div id="poetrydata">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-header style="font-size: 20px;
    height:80px;
    background-color: rgba(84,92,100,0.5);
    color: #333;
    text-align: center;line-height: 40px;">
        <el-row>
          <el-col :span='8' :offset="3">
            <span>发布者：{{ username }}</span><br>
            <span>邮箱：{{ email }}</span>

          </el-col>
          <el-col :span="8">
            <span>性别：{{ sex_data }}</span><br>
            <span>城市：{{ city }}</span>
          </el-col>
          <el-col :span="3">
            <el-button size="small" style="background-color: unset;color:#000000" @click="delete_confirm">删除</el-button>
            <br>
            <router-link to='/myhome' class="ganjing">
              <el-button size="small" style="background-color: unset;color:#000000">返回</el-button>
            </router-link>
          </el-col>
        </el-row>
      </el-header>

      <el-main>
        <el-row>
          <el-col :span="18" :offset="6">
            <el-card class="box-card" style="background-color: rgba(246, 246, 246, 0.5)">
              <div slot="header" style="height: 20px">
                <el-row style="display: flex; justify-content: center;">
                  <el-col :span="3">{{ keyword }}</el-col>
                </el-row>
              </div>
              <el-row style="display: flex; justify-content: center;">
                <el-col style="white-space: pre-wrap">{{ poecontent }}</el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="18" :offset="6">
            <el-card class="box-card" style="background-color: rgba(246, 246, 246, 0.5)">
              <div slot="header" style="height: 20px">
                <span style="float:left">评论：</span>
              </div>
              <div v-for="(item,index) in this.compoemData" :key="index">
                <el-row>
                  <el-col style="float: left">{{ item.fields.username }}:{{ item.fields.comments }}</el-col>
                </el-row>
              </div>
            </el-card>
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
      username: this.COMMON.USERNAME,
      password: '',
      email: '',
      sex: '',
      city: '',
      keyword: '',
      poecontent: '',
      goodnum: '',
      sex_data: '',
      release_id: this.$route.query.release_id,
      relkey: {model: '', pk: '', fields: {keyword: '', poecontent: '', username: '', goodnum: '', mywords: ''}},
      compoemData: []
    }
  },
  mounted: function () {
    this.COMMON.get_baseinformation(this, this.username)
    this.get_releaseinformation()
    this.get_commentinformation()
  },
  methods: {
    get_releaseinformation() {
      console.log(this.release_id)
      this.$http.get('http://120.79.64.45:5000/app1/releaseinfo2', {
        params:
          {release_id: this.release_id}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          console.log(res)
          this.relkey = res['list'][0]
          this.keyword = this.relkey.fields.keyword
          this.poecontent = this.relkey.fields.poecontent
          this.goodnum = this.relkey.fields.goodnum
        })
    },
    get_commentinformation() {
      this.$http.get('http://120.79.64.45:5000/app1/commentinfo', {
        params:
          {release_id: this.release_id}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.compoemData = res['list']
        })
    },
    delete_releaseinformation() {
      this.$http.get('http://120.79.64.45:5000/app1/reldelete', {
        params:
          {release_id: this.release_id}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.$alert(res['msg'], '提示', {
            confirmButtonText: '确定',
            callback: action => {
              this.get_commentinformation()
              this.$router.push({path: '/myhome'})
            }
          })
        })
    },
    delete_confirm() {
      this.$confirm('此操作将删除该作品, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delete_releaseinformation()
      }).catch(() => {

      })
    }
  }
}
</script>

<style scoped>
#poetrydata {
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

.box-card {
  margin-left: 0;
  margin-bottom: 20px;
  width: 700px;
  height: 300px;
  overflow-y: auto;
  text-align: left;
}
</style>
