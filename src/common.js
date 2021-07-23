const USERNAME=''
const TARGET=''

function get_baseinformation(that, username) {
  console.log(username)
  if (username === '') {
    that.$confirm('你还没有登陆，是否登陆？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }).then(() => {
      that.$router.push({path: '/Login'})
    }).catch(() => {
      that.$router.push({path: '/Products'})
    })
  } else {
    that.$http.get('http://120.79.64.45:5000/app1/userinfo', {
      params:
        {username: that.username}
    })
      .then((response) => {
        let res = JSON.parse(response.bodyText)
        that.sex = res['msg'].sex
        if (that.sex === '0') {
          that.sex_data = '男'
        } else {
          that.sex_data = '女'
        }
        that.password=res['msg'].password
        that.email = res['msg'].email
        that.city = res['msg'].city
      })
  }
}
export default {
  USERNAME,
  TARGET,
  get_baseinformation
}
