<template>
  <div class="main">

    <div class="wrap"><h1 class="info">发布作品</h1></div>
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
</template>

<script>
export default {
  name: "index"
}
</script>

<style scoped>

</style>
