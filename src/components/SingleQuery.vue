<template>
<div class="singlequery">
    <Tabs value="name1">
        <TabPane label="公司信息" name="name1">
            <Table :loading="loading" :data="tableData" :columns="tableColumns" stripe size="small" max-height="450"></Table>
            <!--div style="margin: 10px;overflow: hidden">
                <div style="float: right;">
                    <Page :total="100" :current="1" @on-change="changePage"></Page>
                </div>
            </div-->
        </TabPane>
        <TabPane label="单条输入" name="name2">
            <Row>
            <Col span="8">
                <br>
                <Form label-position="left" :label-width="100">
                    <FormItem label="ID">
                        <Input v-model="ID" />
                    </FormItem>
                    <FormItem label="注册时间">
                        <Input v-model="RegistrationTime" />
                    </FormItem>
                    <FormItem label="注册资本">
                        <Input v-model="RegistrationCapital" />
                    </FormItem>
                    <FormItem label="行业">
                        <Select v-model="Industry">
                            <Option value="beijing">New York</Option>
                            <Option value="shanghai">London</Option>
                            <Option value="shenzhen">Sydney</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="区域">
                        <Input v-model="District" />
                    </FormItem>
                    <FormItem label="企业类型">
                        <Input v-model="Type" />
                    </FormItem>
                    <FormItem label="控制人类型">
                        <Input v-model="Ucsp" />
                    </FormItem>
                    <FormItem label="控制人ID">
                        <Input v-model="ControllingPersonID" />
                    </FormItem>
                    <FormItem>
                        <Button @click="SingleInput()" type="primary" long>保存</Button>
                    </FormItem>
                </Form>
            </Col>
            </Row>
        </TabPane>
    </Tabs>
</div>
</template>
<script>
import Axios from 'axios';
export default {
    data () {
        return {
            loading: false,
            ID: '',
            RegistrationTime: '',
            RegistrationCapital: '',
            Industry: '',
            District: '',
            Type: '',
            Ucsp: '',
            ControllingPersonID: '',
            tableData: [],
            tableColumns: [
                {
                    type: 'selection',
                    width: 60,
                    align: 'center',
                    fixed: 'left'
                },
                {
                    title: 'ID',
                    key: 'ID',
                    width: 100,
                    fixed: 'left'
                },
                {
                    title: '注册时间',
                    key: 'RegistrationTime',
                    width: 150
                },
                {
                    title: '注册资本',
                    key: 'RegistrationCapital'
                },
                {
                    title: '行业',
                    key: 'Industry',
                },
                {
                    title: '区域',
                    key: 'District'
                },
                {
                    title: '企业类型',
                    key: 'Type'
                },
                {
                    title: '控制人类型',
                    key: 'Ucsp'
                },
                {
                    title: '控制人ID',
                    key: 'ControllingPersonID',
                    width: 200
                },
                {
                    title: '...',
                    key: '...'
                },
                {
                    title: '操作',
                    key: '操作',
                    width: 200,
                    align: 'center',
                    fixed: 'right',
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'success',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                        this.show(params.index)
                                    }
                                }
                            }, '预测'),
                            h('Button', {
                                props: {
                                    type: 'primary',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                        this.remove(params.index)
                                    }
                                }
                            }, '编辑'),
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'small'
                                },
                                on: {
                                    click: () => {
                                        this.remove(params.index)
                                    }
                                }
                            }, '删除')
                        ]);
                    }
                },
                {
                    title: '结果',
                    key: '结果',
                    fixed: 'right'
                }
            ]
        }
    },
    methods: {
        SingleInput() {
            var api = this.$api_baseUrl + 'SingleInput'
            var data = {
                'ID': this.ID,
                'RegistrationTime': this.RegistrationTime,
                'RegistrationCapital': this.RegistrationCapital,
                'Industry': this.Industry,
                'District': this.District,
                'Type': this.Type,
                'Ucsp': this.Ucsp,
                'ControllingPersonID': this.ControllingPersonID,
            }
            Axios.post(api, data).then((res)=>{
                this.$Message['info']({
                    background: true,
                    content: res.data
                });
            }).finally(()=>{
                this.getCompanyInfo()
            })
        },
        getCompanyInfo() {
            var api = this.$api_baseUrl + 'getCompanyInfo'
            this.loading = true
            Axios.get(api).then((res)=>{
                this.tableData = res.data
                this.loading = false
            })
        },
        remove (index) {
            this.tableData.splice(index, 1);
        },
        /*
        changePage () {
            // The simulated data is changed directly here, and the actual usage scenario should fetch the data from the server
        }
        */
    },
    mounted() {
        this.getCompanyInfo()
    }
}
</script>