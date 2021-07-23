<!--我的收藏-->
<template>
  <div id="mycollection">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <el-header style=" background-color: rgba(84,92,100,0.5);
          color: #333;
          text-align: center;
          line-height: 60px;">
        <el-row>
          <el-col :span="6" :offset="8">
            <div>我收藏的诗歌</div>
          </el-col>
          <el-col :span="2" :offset="8">
            <router-link to='/myhome'>
              <el-button size="small" style="background-color: unset;color:#000000">返回</el-button>
            </router-link>
          </el-col>
        </el-row>
      </el-header>

      <el-main>
        <el-col :span="24">
          <div v-for="(item,index) in this.poemData" :key="index">
            <el-col :span="12">
              <el-card class="box-card">
                <div slot="header" style="height: 40px">
                  <el-row style="display: flex; justify-content: center;">

                    <el-col>{{ item.fields.keyword }}</el-col>
                  </el-row>
                  <el-row style="float: right">
                    <el-col :span="5">
                      <el-button size="mini" style="background-color: rgba(246, 246, 246, 0.7);color:#000000"
                                 @click="delete_confirm(item.pk)">删除作品
                      </el-button>
                    </el-col>
                  </el-row>
                </div>
                <el-row style="display: flex; justify-content:center;align-items: center;height: 180px">
                  <el-col style="white-space: pre-wrap">{{ item.fields.poecontent }}</el-col>
                </el-row>
              </el-card>
            </el-col>
          </div>
        </el-col>
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
      poemData: [],
      pk: ''
    }
  },
  mounted: function () {
    this.prt_collection()
  },
  methods: {
    prt_collection() {
      this.$http.get('http://120.79.64.45:5000/app1/collprint', {
        params:
          {username: this.username}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.poemData = res['list']
        })
    },
    delete_poem(pk) {
      this.$http.get('http://120.79.64.45:5000/app1/colldelete', {
        params:
          {pk: pk}
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          this.$alert(res['msg'], '提示', {
            confirmButtonText: '确定',
            callback: action => {
              this.prt_collection()
            }
          })
          this.delete_notice()
        })
    },
    delete_confirm(pk) {
      this.$confirm('此操作将删除该收藏, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.delete_poem(pk)
      }).catch(() => {

      })
    },
    delete_notice() {
      this.$alert(this.response['msg'], '提示', {
        confirmButtonText: '确定',
        callback: action => {
          this.prt_collection()
        }
      })
    }
  }
}

</script>
<style scoped>
#mycollection {
  background-image: url('../assets/p2.jpg');
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

.box-card {
  margin-left: 20px;
  margin-bottom: 20px;
  width: 500px;
  height: 300px;
  background-color: rgba(246, 246, 246, 0.5);
}
</style>

