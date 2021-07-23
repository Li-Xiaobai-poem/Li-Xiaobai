<template>
  <div id="a">
    <app-header></app-header>
    <app-navbar></app-navbar>

    <div class="main"><h1 class="info">发布作品</h1>
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="标题" prop="_title">
          <el-input type="text" v-model="ruleForm._title" autocomplete="off" placeholder="请输入标题"></el-input>
        </el-form-item>
        <el-form-item label="正文" prop="_content">
          <el-input type="textarea" v-model="ruleForm._content" autocomplete="off" placeholder="请输入正文"></el-input>
        </el-form-item>
        <el-form-item label="文字" prop="_words">
          <el-input v-model.number="ruleForm._words" placeholder="请输入想说的话"></el-input>
        </el-form-item>
        <el-form-item style="width: 400px;margin: 0 auto">
          <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>

    </div>
  </div>
</template>

<script>

import AppHeader from "./AppHeader"
import AppNavbar from "./AppNavbar"

import axios from "axios"

export default {
  name: "Publisher", components: {AppHeader, AppNavbar},
  data() {
    var checkTitle = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('标题不能为空'));
      }
      callback();
    };
    var validateContent = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入内容'));
      } else {
        callback();
      }
    };
    var validateWords = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入想说的话'));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        _words: '',
        _content: '',
        _title: ''
      },
      rules: {
        _title: [
          {validator: checkTitle, trigger: 'blur'}
        ],
        _content: [
          {validator: validateContent, trigger: 'blur'}
        ],
        _words: [
          {validator: validateWords, trigger: 'blur'}
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {

          axios.post("http://120.79.64.45:5000/publisher/",
            {
              "title": this.ruleForm._title,
              "content": this.ruleForm._content,
              "words": this.ruleForm._words
            }
          ).then((res) => {
            console.log("ok.")
            this.$message.info("提交成功。")
          }).catch((err) => {
            console.log(err)
          })

        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main {
  position: absolute;
  top: 50px;
  left: 230px;
  bottom: 0px;
  right: 0px; /* 距离右边0像素 */
  padding: 10px;
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

#a{
  background-image: url('../assets/p7.jpg');
  background-repeat: round;
  position: fixed;
  width: 100%;
  height: 100vh;
  overflow: auto;
}
</style>


