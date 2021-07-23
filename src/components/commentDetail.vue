<template>
  <div id="ab">
    <app-header></app-header>
    <app-navbar></app-navbar>
    <el-container class="main">
      <!--    导航栏 返回 -->

      <!--    输入框-->
      <el-button size="small" @click="goBack" id="aaa">返回</el-button>

      <el-main>
        <el-row>
        <el-col :span="18">
          <el-input
            type="textarea"
            :rows="3"
            placeholder="请输入想说的话"
            v-model="textarea">
          </el-input>
        </el-col>
        <el-col :span="2" style="text-align:center;">
          <el-button type="primary" @click="say" style="background-color: unset;color:#000000">发布</el-button>
        </el-col>
        </el-row>

      <!--    评论显示-->
      <!--      <el-main>-->
      <!--        <div v-for="(item,index) in this.items"  :key="index">-->
      <!--         <a  >{{item.fields.username}} </a>-->
      <!--            <span>{{item.fields.comments}}</span>-->
      <!--             <br>-->
      <!--        </div>-->
      <!--      </el-main>-->

        <el-row>
          <el-col :span="18">
<!--            <el-card class="box-card" style="float: left" id="a2">-->
<!--              <div slot="header" class="clearfix">-->
<!--                <span style="float:left">评论：</span>-->
<!--              </div>-->
<!--              <div v-for="(item,index) in this.items" :key="index" style="background-color: unset;color:#000000">-->
<!--                <el-row>-->
<!--                  <el-col style="float: left">{{ item.fields.username }}:{{ item.fields.comments }}</el-col>-->
<!--                </el-row>-->

<!--              </div>-->
<!--            </el-card>-->
            <el-card class="box-card" style="background-color: rgba(246, 246, 246, 0.5)">
              <div slot="header" style="height: 20px">
                <span style="float:left">评论：</span>
              </div>
              <div v-for="(item,index) in this.items" :key="index">
                <el-row>
                  <el-col style="float: left">{{ item.fields.username }}:{{ item.fields.comments }}</el-col>
                </el-row>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>


      <!--      底部页码栏-->
      <el-footer class="footer">
      </el-footer>
    </el-container>

  </div>
</template>

<script>
import AppHeader from "./AppHeader"
import AppNavbar from "./AppNavbar"


export default {
  name: "comment", components: {AppHeader, AppNavbar},

  data() {
    return {
      textarea: '',
      items: [],
      target: this.COMMON.TARGET
    }
  },
  mounted: function () {
    this.showComments()
  }
  ,
  methods: {
    goBack() {
      this.$router.push({path: '/LunTan'})
    },
    showComments() {
      console.log(this.target)
      this.$http.get('http://120.79.64.45:5000/app1/showComments', {params: {rel_id: this.target}}, {
        emulateJSON: true
      })
        .then((response) => {

          let res = JSON.parse(response.bodyText)

          if (res['error_num'] === 0) {


            this.items = res['comlist']


            console.log("成功")


          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })
    },
    say() {

      if (this.COMMON.USERNAME === '') {
        this.$confirm('你还没有登陆，是否登陆？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$router.push({path: '/Login'})
        }).catch(() => {

        })
      } else {
        if (this.textarea === "") {

        } else {
          console.log(this.target)
          this.$http.get('http://120.79.64.45:5000/app1/addComments', {
            params: {
              rel_id: this.target,
              saywords: this.textarea,
              username: this.COMMON.USERNAME
            }
          }, {
            emulateJSON: true
          })
            .then((response) => {

              let res = JSON.parse(response.bodyText)

              if (res['error_num'] === 0) {


                this.showComments()
                this.textarea = ""

              } else {

                console.log(res['msg'])
              }
            })
        }
      }

    }

  }

}
</script>

<style scoped>
a {
  text-decoration: none;
}

.footer {
  margin-left: 300px;
  margin-bottom: 60px;

  position: absolute;
  bottom: 0;
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

#aaa {
  width: 100px;

}

.box-card {
  margin-left:10px;
  margin-bottom: 20px;
  width: 1000px;
  height: 300px;
  overflow-y: auto;
   text-align: left;
}
#ab{
   background-image: url('../assets/p6.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
}

</style>
