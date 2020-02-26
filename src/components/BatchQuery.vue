<template>
<div class="batchquery">
<Breadcrumb style="text-align:left;margin:5px 0px 10px 10px">
    <BreadcrumbItem>
        系统菜单
    </BreadcrumbItem>
    <BreadcrumbItem>
        <Icon type="ios-search" />
        批量查询
    </BreadcrumbItem>
</Breadcrumb>
<Card dis-hover>
    <Tabs value="name1">
        <TabPane label="批量查询" name="name1">
            <br>
            <Row type="flex" justify="space-around" align="top">
                <Col :md="6" :xs="24" style="text-align:left;margin:16px 0px;">
                    <Form label-position="left" :label-width="100">
                        <p style="color:#ed4014;">请按照提示上传相应文件</p>
                        <br>
                        <FormItem label="基本信息：">
                            <Upload 
                                :action="this.$api_baseUrl+'Upload'" 
                                ref="base" 
                                :data="this.UploadParams"
                                :before-upload="(file)=>beforeUpload(file,1)" 
                                :on-success="(response,file,fileList,i)=>uploadSuccess(response,file,fileList,1)"
                                :on-error="uploadError"
                                :max-size="20 * 1024"
                                :on-exceeded-size="handleMaxSize"
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
                                :on-success="(response,file,fileList,i)=>uploadSuccess(response,file,fileList,2)"
                                :on-error="uploadError"
                                :max-size="20 * 1024"
                                :on-exceeded-size="handleMaxSize"
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
                                :on-success="(response,file,fileList,i)=>uploadSuccess(response,file,fileList,3)"
                                :on-error="uploadError"
                                :max-size="20 * 1024"
                                :on-exceeded-size="handleMaxSize"
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
                                :on-success="(response,file,fileList,i)=>uploadSuccess(response,file,fileList,4)"
                                :on-error="uploadError"
                                :max-size="20 * 1024"
                                :on-exceeded-size="handleMaxSize"
                                accept=".csv"
                                >
                                <Button icon="ios-cloud-upload-outline" v-if="!money_info">选择文件</Button>
                                <Button icon="ios-cloud-upload-outline" v-else>{{ this.money_info.name }}</Button>
                                <div slot="tip" style="color:#808695;">支持拓展名: .csv</div>
                            </Upload>
                        </FormItem>
                            <Button type="success" style="width:200px;"  @click="upload">提交</Button>
                            <!--Button type="error" size="normal" style="width:100px; marginLeft:25px;" @click="clear">清空</Button-->
                    </Form>
                </Col>
                <Col :md="16" :xs="24" style="margin:16px 0px;">
                    <Table :data="tableData1" :columns="tableColumns1" stripe max-height="470"></Table>
                </Col>
            </Row>
            <br>
        </TabPane>
    </Tabs>
</Card>
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
            base_success: false,
            paient_info_success: false,
            year_report_success: false,
            money_info_success: false,
            UploadParams: {},
            tableColumns1: [
                {
                    title: '编号',
                    key: 'ID',

                },
                {
                    title: '提交时间',
                    key: 'CreatTime',

                },
                {
                    title: '提交状态',
                    key: 'PredictState',

                    render: (h, params) => {
                        return h('Tag', {
                            props:{
                                type: 'dot',
                                color: params.row['PredictState']==1 ? 'success' : params.row['PredictState']==0 ? 'warning' : 'error'
                            }
                        }, params.row['PredictState']==1 ? '预测成功': params.row['PredictState']==0 ? '预测中...': '文件错误')
                    }
                },
                {
                    title: '操作',
                    key: '操作',

                    render: (h, params) => {
                        if(params.row['PredictState']==0){
                            return h('Button',{
                                props: {
                                    type: 'warning',
                                    long: true,
                                    shape: 'circle',
                                    loading: true,
                                }
                            }, '')
                        }else{
                            return h('div', [
                                h('Button', {
                                    props: {
                                        //icon: "ios-download-outline",
                                        type: "primary",
                                        disabled: params.row['PredictState']==1 ? false : true
                                    },
                                    style: {
                                        marginRight: '10px'
                                    },
                                    on: {
                                        click: () => {
                                            this.download(this.tableData1[params.index]['FilePath'])
                                        }
                                    }
                                }, '下载'),
                                h('Button', {
                                    props:{
                                        type: 'error'
                                    },
                                    on: {
                                        click: () => {
                                            this.beforeDelete(this.tableData1[params.index]['FilePath'])
                                            //this.delete(this.tableData1[params.index]['FilePath'])
                                        }
                                    }
                                }, '删除')
                            ])
                        }
                    }
                }
            ],
            tableData1: []
        }
    },
    methods: {
        getTime() {
            let now = new Date()
            let yy = now.getFullYear()+'';
            let mm = now.getMonth()+1<10 ? '0'+(now.getMonth()+1) : now.getMonth()+1+''
            let dd = now.getDate()<10 ? '0'+now.getDate() : now.getDate()+''
            let hh = now.getHours()<10 ? '0'+now.getHours() : now.getHours()+'' 
            let mf = now.getMinutes()<10 ? '0'+now.getMinutes() : now.getMinutes()+''
            let ss = now.getSeconds()<10 ? '0'+now.getSeconds() : now.getSeconds()+''
            return yy+'-'+mm+'-'+dd+'-'+hh+mf+ss
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
        handleMaxSize (file) {
            this.$Notice.warning({
                title: '文件大小超限',
                desc: '文件  ' + file.name + ' 太大，上传文件大小不能超过20M.'
            });
        },
        uploadSuccess(response,file,fileList,i) {
            if(i==1)        this.base_success = true
            else if(i==2)   this.paient_info_success = true
            else if(i==3)   this.year_report_success = true
            else if(i==4)   this.money_info_success = true
            if(this.base_success && this.paient_info_success && this.year_report_success && this.money_info_success){
                this.base_success = false
                this.paient_info_success = false
                this.year_report_success = false
                this.money_info_success = false
                this.getBatchRecord()
                setTimeout(() => {
                    this.clear()
                }, 1000);
                this.timeout = setInterval(()=>{
                    this.updatePredictState(this.UploadParams.filepath)
                }, 1000*1)
            }
        },
        upload() {
            if(this.base && this.paient_info && this.year_report && this.money_info){
                this.UploadParams.filepath = this.getTime()
                this.UploadParams.type = 'base'
                this.$refs.base.post(this.base)
                this.UploadParams.type = 'paient_info'
                this.$refs.paient_info.post(this.paient_info)
                this.UploadParams.type = 'year_report'
                this.$refs.year_report.post(this.year_report)
                this.UploadParams.type = 'money_info'
                this.$refs.money_info.post(this.money_info)

                this.base = ''
                this.paient_info = ''
                this.year_report = ''
                this.money_info = ''
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
        uploadError(error, file, fileList){
            this.$Notice.error({
                title: '上传失败，请重试或联系管理员！'
            });
        },
        updatePredictState(filepath){
            //console.log('执行定时任务')
            var api = this.$api_baseUrl + 'getPredictState/' + filepath
            Axios.get(api).then((res)=> {
                //console.log(res.data)
                if(res.data=='True'){
                    this.getBatchRecord()
                    clearInterval(this.timeout)
                }
            })
        },
        download(filepath) {
            var url = this.$api_baseUrl + 'Download/' + filepath
            let a = document.createElement('a')
            a.href = url
            a.click();
        },
        beforeDelete(filepath) {
            this.$Modal.confirm({
                        title: '删除确认',
                        content: '您确认要删除此条记录吗？',
                        onOk: () => {
                            this.delete(filepath)
                        }
                    });
        },
        delete(filepath) {
            var api = this.$api_baseUrl + 'Delete'
            var data = {
                FilePath: filepath
            }
            Axios.post(api, data).then((res)=>{
                this.getBatchRecord()
            })
        }
    },
    mounted() {
        this.getBatchRecord()
    }
}
</script>