<template>
<div class="singlequery">
    <Tabs value="name1">
        <TabPane label="公司信息" name="name1">
            <Table :data="tableData1" :columns="tableColumns1" stripe size="large" max-height="700"></Table>
            <div style="margin: 10px;overflow: hidden">
                <div style="float: right;">
                    <Page :total="100" :current="1" @on-change="changePage"></Page>
                </div>
            </div>
        </TabPane>
        <TabPane label="单条输入" name="name2">
            <Row>
            <Col span="8">
                <br>
                <Form label-position="left" :label-width="100">
                    <FormItem label="ID">
                        <Input v-model="input1" />
                    </FormItem>
                    <FormItem label="注册时间">
                        <Input v-model="input2" />
                    </FormItem>
                    <FormItem label="注册资本">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem label="行业">
                        <Select v-model="select">
                            <Option value="beijing">New York</Option>
                            <Option value="shanghai">London</Option>
                            <Option value="shenzhen">Sydney</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="区域">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem label="企业类型">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem label="控制人类型">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem label="控制人ID">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem label="注册资本">
                        <Input v-model="input3" />
                    </FormItem>
                    <FormItem>
                        <Button type="primary" long>保存</Button>
                    </FormItem>
                </Form>
            </Col>
            </Row>
        </TabPane>
    </Tabs>
</div>
</template>
<script>
    export default {
        data () {
            return {
                input1: '',
                input2: '',
                input3: '',
                select: '',
                tableData1: this.mockTableData1(),
                tableColumns1: [
                    {
                        type: 'selection',
                        width: 60,
                        align: 'center',
                        fixed: 'left'
                    },
                    {
                        title: 'ID',
                        key: 'name',
                        width: 100,
                        fixed: 'left'
                    },
                    {
                        title: '注册时间',
                        key: '注册时间',
                        render: (h, params) => {
                            const row = params.row;
                            const color = row.status === 1 ? 'primary' : row.status === 2 ? 'success' : 'error';
                            const text = row.status === 1 ? 'Working' : row.status === 2 ? 'Success' : 'Fail';

                            return h('Tag', {
                                props: {
                                    type: 'dot',
                                    color: color
                                }
                            }, text);
                        }
                    },
                    {
                        title: '注册资本',
                        key: '注册资本',
                        render: (h, params) => {
                            return h('Poptip', {
                                props: {
                                    trigger: 'hover',
                                    title: params.row.portrayal.length + 'portrayals',
                                    placement: 'bottom'
                                }
                            }, [
                                h('Tag', params.row.portrayal.length),
                                h('div', {
                                    slot: 'content'
                                }, [
                                    h('ul', this.tableData1[params.index].portrayal.map(item => {
                                        return h('li', {
                                            style: {
                                                textAlign: 'center',
                                                padding: '4px'
                                            }
                                        }, item)
                                    }))
                                ])
                            ]);
                        }
                    },
                    {
                        title: '行业',
                        key: '行业',
                        render: (h, params) => {
                            return h('Poptip', {
                                props: {
                                    trigger: 'hover',
                                    title: params.row.people.length + 'customers',
                                    placement: 'bottom'
                                }
                            }, [
                                h('Tag', params.row.people.length),
                                h('div', {
                                    slot: 'content'
                                }, [
                                    h('ul', this.tableData1[params.index].people.map(item => {
                                        return h('li', {
                                            style: {
                                                textAlign: 'center',
                                                padding: '4px'
                                            }
                                        }, item.n + '：' + item.c + 'People')
                                    }))
                                ])
                            ]);
                        }
                    },
                    {
                        title: '区域',
                        key: '区域',
                        render: (h, params) => {
                            return h('div', 'Almost' + params.row.time + 'days');
                        }
                    },
                    {
                        title: '企业类型',
                        key: '企业类型',
                        render: (h, params) => {
                            return h('div', this.formatDate(this.tableData1[params.index].update));
                        }
                    },
                    {
                        title: '控制人类型',
                        key: '控制人类型',
                        render: (h, params) => {
                            return h('div', this.formatDate(this.tableData1[params.index].update));
                        }
                    },
                    {
                        title: '控制人持股比例',
                        key: '控制人持股比例',
                        width: 200,
                        render: (h, params) => {
                            return h('div', this.formatDate(this.tableData1[params.index].update));
                        }
                    },
                    {
                        title: '...',
                        key: '...',
                        render: (h, params) => {
                            return h('div', this.formatDate(this.tableData1[params.index].update));
                        }
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
                                    style: {
                                        marginRight: '5px'
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
            mockTableData1 () {
                let data = [];
                for (let i = 0; i < 10; i++) {
                    data.push({
                        name: 'Business' + Math.floor(Math.random () * 100 + 1),
                        status: Math.floor(Math.random () * 3 + 1),
                        portrayal: ['City', 'People', 'Cost', 'Life', 'Entertainment'],
                        people: [
                            {
                                n: 'People' + Math.floor(Math.random () * 100 + 1),
                                c: Math.floor(Math.random () * 1000000 + 100000)
                            },
                            {
                                n: 'People' + Math.floor(Math.random () * 100 + 1),
                                c: Math.floor(Math.random () * 1000000 + 100000)
                            },
                            {
                                n: 'People' + Math.floor(Math.random () * 100 + 1),
                                c: Math.floor(Math.random () * 1000000 + 100000)
                            }
                        ],
                        time: Math.floor(Math.random () * 7 + 1),
                        update: new Date(),
                        结果: '僵尸企业'
                    })
                }
                return data;
            },
            formatDate (date) {
                const y = date.getFullYear();
                let m = date.getMonth() + 1;
                m = m < 10 ? '0' + m : m;
                let d = date.getDate();
                d = d < 10 ? ('0' + d) : d;
                return y + '-' + m + '-' + d;
            },
            remove (index) {
                this.tableData1.splice(index, 1);
            },
            changePage () {
                // The simulated data is changed directly here, and the actual usage scenario should fetch the data from the server
                this.tableData1 = this.mockTableData1();
            }
        }
    }
</script>