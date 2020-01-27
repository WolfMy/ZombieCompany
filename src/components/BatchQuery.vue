<template>
<div class="batchquery">
    <Tabs value="name1">
        <TabPane label="批量查询" name="name1">
            <br>
            <Row>
                <Col span="8" style="text-align:left;">
                    <Form label-position="left" :label-width="100">
                        <p style="color:#ed4014;">请按照提示上传相应文件</p>
                        <br>
                        <FormItem label="基本信息：">
                            <Upload 
                                :action="this.$api_baseUrl+'Upload'" 
                                ref="base" 
                                :data="this.UploadParams"
                                :before-upload="(file)=>beforeUpload(file,1)" 
                                :on-success="uploadSuccess"
                                :on-error="uploadError"
                                accept=".csv"
                                >
                                <Button icon="ios-cloud-upload-outline" v-if="!base">选择文件</Button>
                                <Button icon="ios-cloud-upload-outline" v-else>{{ this.base.name }}</Button>
                                <div slot="tip" style="color:#808695;">支持拓展名: .csv</div>
                            </Upload>
                        </FormItem>
                        <FormItem label="知识产权：">
                            <Upload
                                :action="this.$api_baseUrl+'Upload'" 
                                ref="paient_info" 
                                :data="this.UploadParams"
                                :before-upload="(file)=>beforeUpload(file,2)" 
                                :on-success="uploadSuccess"
                                :on-error="uploadError"
                                accept=".csv"
                                >
                                <Button icon="ios-cloud-upload-outline" v-if="!paient_info">选择文件</Button>
                                <Button icon="ios-cloud-upload-outline" v-else>{{ this.paient_info.name }}</Button>
                                <div slot="tip" style="color:#808695;">支持拓展名: .csv</div>
                            </Upload>
                        </FormItem>
                        <FormItem label="年报：">
                            <Upload
                                :action="this.$api_baseUrl+'Upload'" 
                                ref="year_report" 
                                :data="this.UploadParams"
                                :before-upload="(file)=>beforeUpload(file,3)" 
                                :on-success="uploadSuccess"
                                :on-error="uploadError"
                                accept=".csv"
                                >
                                <Button icon="ios-cloud-upload-outline" v-if="!year_report">选择文件</Button>
                                <Button icon="ios-cloud-upload-outline" v-else>{{ this.year_report.name }}</Button>
                                <div slot="tip" style="color:#808695;">支持拓展名: .csv</div>
                            </Upload>
                        </FormItem>
                        <FormItem label="融资信息：">
                            <Upload
                                :action="this.$api_baseUrl+'Upload'" 
                                ref="money_info" 
                                :data="this.UploadParams"
                                :before-upload="(file)=>beforeUpload(file,4)" 
                                :on-success="uploadSuccess"
                                :on-error="uploadError"
                                accept=".csv"
                                >
                                <Button icon="ios-cloud-upload-outline" v-if="!money_info">选择文件</Button>
                                <Button icon="ios-cloud-upload-outline" v-else>{{ this.money_info.name }}</Button>
                                <div slot="tip" style="color:#808695;">支持拓展名: .csv</div>
                            </Upload>
                        </FormItem>
                            <Button type="success" size="large" style="width:100px;" @click="upload">提交</Button>
                            <Button type="error" size="large" style="width:100px; marginLeft:25px;" @click="clear">清空</Button>

                    </Form>
                </Col>
                <Col span="12">
                    <Table :data="tableData1" :columns="tableColumns1" stripe size="large" max-height="700"></Table>
                </Col>
            </Row>
        </TabPane>
    </Tabs>
</div>
</template>

<script>
import Axios from 'axios'
export default {
    data() {
        return {
            base: '',
            paient_info: '',
            year_report: '',
            money_info: '',
            UploadParams: {},
            tableColumns1: [
                {
                    title: '编号',
                    key: 'ID'
                },
                {
                    title: '提交时间',
                    key: 'CreatTime',
                    width: 200
                },
                {
                    title: '提交结果',
                    key: '提交结果',
                    render: (h, params) => {
                        return h('Tag', {
                            props:{
                                type: 'dot',
                                color: 'success'
                            }
                        }, '预测成功')
                    }
                },
                {
                    title: '操作',
                    key: '操作',
                    render: (h, params) => {
                        return h('Button',{
                            props: {
                                type: 'success',
                            },
                            on: {
                                click: () => {
                                    //this.download(this.tableData1[params.index]['FilePath'])
                                    this.getPredictState(this.tableData1[params.index]['FilePath'])
                                }
                            }
                        }, '下载')
                    }
                },
            ],
            tableData1: []
        }
    },
    methods: {
        getTime() {
            let now = new Date()
            let yy = now.getFullYear();
            let mm = now.getMonth()+1
            let dd = now.getDate()
            let hh = now.getHours()
            let mf = now.getMinutes()<10 ? '0'+now.getMinutes() : now.getMinutes()
            let ss = now.getSeconds()<10 ? '0'+now.getSeconds() : now.getSeconds()
            return yy+''+mm+dd+hh+mf+ss
        },
        getBatchRecord() {
            var api = this.$api_baseUrl + 'getBatchRecord'
            Axios.get(api).then((res)=>{
                this.tableData1 = res.data
            })
        },
        beforeUpload(file,i) {
            let exceededNum=file.name.lastIndexOf(".")
            let exceededStr=file.name.substring(exceededNum+1,file.name.length).trim()
            if(exceededStr!="csv"){
                this.$Notice.warning({
                    title: '文件格式错误',
                    desc: file.name + '文件格式不正确, 请选择 .csv'
                });
                return false
            }else{
                if(i==1)        this.base = file
                else if(i==2)   this.paient_info = file
                else if(i==3)   this.year_report = file
                else if(i==4)   this.money_info = file
            }
            return false
        },
        upload() {
            if(this.base && this.paient_info && this.year_report && this.money_info){
                this.UploadParams.time = this.getTime()
                this.UploadParams.type = 'base'
                this.$refs.base.post(this.base)
                this.UploadParams.type = 'paient_info'
                this.$refs.paient_info.post(this.paient_info)
                this.UploadParams.type = 'year_report'
                this.$refs.year_report.post(this.year_report)
                this.UploadParams.type = 'money_info'
                this.$refs.money_info.post(this.money_info)
                var api = this.$api_baseUrl + 'addBatchRecord'
                var data = {
                    FilePath: this.UploadParams.time
                }
                Axios.post(api, data).then((res)=>{
                    this.getBatchRecord()
                })
            }else
                this.$Notice.warning({
                    title: '文件缺失',
                    desc: '请上传基本信息、知识产权、年报、融资信息4个文件后，再点击提交！'
                });
        },
        clear() {
            this.base = ''
            this.paient_info = ''
            this.year_report = ''
            this.money_info = ''
            this.$refs.base.clearFiles()
            this.$refs.paient_info.clearFiles()
            this.$refs.year_report.clearFiles()
            this.$refs.money_info.clearFiles()
        },
        uploadSuccess(response, file, fileList){
            //可在此设置定时任务，检测“提交结果”
        },
        uploadError(error, file, fileList){
            this.$Notice.error({
                title: '上传失败，请重试或联系管理员！'
            });
        },
        getPredictState(filepath){
            var api = this.$api_baseUrl + 'getPredictState/' + filepath
            Axios.get(api).then((res)=> {
                console.log(res.data)
                
            })
        },
        download(filepath) {
            var url = this.$api_baseUrl + 'Download/' + filepath
            let a = document.createElement('a')
            a.href = url
            a.click();
        }
    },
    mounted() {
        this.getBatchRecord()
    }
}
</script>