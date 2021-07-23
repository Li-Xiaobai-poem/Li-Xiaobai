<template>
  <div id="app">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <!--外层大容器-->
    <el-container class="main" style=" border: 1px solid #eee;">


      <!--    右侧继续定义一个容器 -->
      <el-container>


        <div v-for="(item,index) in this.items" :key="index">
          <el-row :gutter="10">

            <el-col :span="2" style="text-align:left">
              <el-col :span="12">
                <el-avatar> {{ item.fields.username }}</el-avatar>
                <p class="date"> {{ item.fields.keyword }} </p>
              </el-col>
            </el-col>
            <!--          诗词正文部分-->
            <el-col :span="18">
              <el-input
                type="textarea"
                :rows="5" cols="10"
                placeholder="诗词正文"
                v-model="item.fields.poecontent"
                readonly="readonly" resize="none" style="background-color: unset;color:#000000">
              </el-input>
            </el-col>
          </el-row>
          <!--          </el-main>-->
          <!--      评论显示-->
          <!--          <el-main style="text-align:left" >-->
          <div class='com'>
            <!--              <a  >SirenGatti: </a>-->
            <!--              <span>{{com1}}</span>-->
            <!--              <br>-->
            <!--              <a  >SirenGatti: </a>-->
            <!--              <span>{{com2}}</span>-->
            <!--              <br>-->
            <!--              <a >SirenGatti: </a>-->
            <!--              <span>{{com3}}</span>-->
          </div>
          <!--          </el-main>-->
          <!--      互动区，包括点赞收藏评论-->
          <!--          <el-main>-->
          <el-row :gutter="20">
            <!--              <el-col :span="4" style="text-align:center">-->
            <!--                <el-badge :value="item.fields.goodnum" class="item">-->
            <!--                  <el-button size="small">点赞</el-button>-->
            <!--                </el-badge>-->
            <!--              </el-col>-->
            <el-col :span="12" style="text-align:center">
              <el-badge class="item">
                <el-button style="background-color: unset;color:#000000" size="small" @click="showdetail(item.pk)">评论
                </el-button>
              </el-badge>
            </el-col>
            <el-col :span="4" style="text-align:center">
              <el-badge class="item">
                <el-button style="background-color: unset;color:#000000" size="small"
                           @click="finalopen(item.fields.poecontent,item.fields.keyword)">收藏
                </el-button>
              </el-badge>
            </el-col>
          </el-row>

          <el-col>
            <el-divider></el-divider>
          </el-col>
        </div>


        <el-footer style="text-align:center">
        </el-footer>
      </el-container>
    </el-container>

  </div>
</template>

<script>
import AppHeader from "./AppHeader"
import AppNavbar from "./AppNavbar"

export default {
  name: "Luntan", components: {AppHeader, AppNavbar},

  data() {
    return {
      num: 1,
      pk: '',
      items: [],
      receive: {
        model: '',
        release_id: '',
        fields: {keyword: '', poecontent: '', username: '', goodnum: '', mywords: ''}
      }
    };
  },

  mounted: function () {
    this.showLuntan()
  },
  methods: {
    //   handleChange(value) {
    //     console.log(value);
    //   },


    showLuntan() {
      // 'http://127.0.0.1:8000/app1/getResult?q='   本地运行地址
      this.$http.get('http://120.79.64.45:5000/app1/showLuntan')
        .then((response) => {
          let res = JSON.parse(response.bodyText)

          if (res['error_num'] === 0) {


            this.items = res['reallist']


            console.log("成功")


          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })
    },
    finalopen(poemcontent, keyword) {
      if(this.COMMON.USERNAME===''){
        this.$confirm('你还没有登陆，是否登陆？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$router.push({path: '/Login'})
        }).catch(() => {

        })
      }else{
        this.$confirm('确定收藏？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.open(poemcontent, keyword)
      }).catch(() => {

      })}

    },

    open(poemcontent, keyword) {

      // 'http://127.0.0.1:8000/app1/getResult?q='   本地运行地址
      this.$http.get('http://120.79.64.45:5000/app1/addcollect1', {
        params: {
          username: this.COMMON.USERNAME,
          poemcontent: poemcontent,
          keyword: keyword
        }
      }, {
        emulateJSON: true
      })
        .then((response) => {
          let res = JSON.parse(response.bodyText)
          if (res['error_num'] === 0) {
            this.$alert('收藏成功', '提示', {
              confirmButtonText: '确定',
              callback: action => {

              }
            })
            console.log("收藏成功了")
          } else {
            this.$alert('收藏失败', '提示', {
              confirmButtonText: '确定',
              callback: action => {

              }
            })
            console.log(res['msg'])
          }
        })


    },
    showdetail(a) {
      this.COMMON.TARGET = a
      this.$router.push({path: '/commentDetail'})

    }


  }

}
</script>

<style scoped>

#app{
  background-image: url('../assets/p4.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
}

a {
  text-decoration: none;
}

.item {
  margin-top: 10px;
  margin-right: 40px;
}

.date {
  font-weight: 50;
  font-size: 5px;
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

/*  ::-webkit-scrollbar {*/
/*  width: 0 !important;*/
/*}*/
/*::-webkit-scrollbar {*/
/*  width: 0 !important;height: 0;*/
/*}*/
a {
  align: left;
}

.com {
  text-align: left;
}
</style>
