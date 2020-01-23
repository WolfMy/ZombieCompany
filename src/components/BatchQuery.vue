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
                            <Upload action="//jsonplaceholder.typicode.com/posts/">
                                <Button icon="ios-cloud-upload-outline">Upload files</Button>
                            </Upload>
                            <p style="color:#808695;">支持拓展名: .csv</p>
                        </FormItem>
                        <FormItem label="知识产权：">
                            <Upload action="//jsonplaceholder.typicode.com/posts/">
                                <Button icon="ios-cloud-upload-outline">Upload files</Button>
                            </Upload>
                            <p style="color:#808695;">支持拓展名: .csv</p>
                        </FormItem>
                        <FormItem label="年报：">
                            <Upload action="//jsonplaceholder.typicode.com/posts/">
                                <Button icon="ios-cloud-upload-outline">Upload files</Button>
                            </Upload>
                            <p style="color:#808695;">支持拓展名: .csv</p>
                        </FormItem>
                        <FormItem label="融资信息：">
                            <Upload action="//jsonplaceholder.typicode.com/posts/">
                                <Button icon="ios-cloud-upload-outline">Upload files</Button>
                            </Upload>
                            <p style="color:#808695;">支持拓展名: .csv</p>
                        </FormItem>
                        <FormItem>
                            <Button type="primary" size="large" style="width:100px;">提交</Button>
                        </FormItem>
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
export default {
    data() {
        return {
            tableColumns1: [
                {
                    title: '编号',
                    key: '编号'
                },
                {
                    title: '提交时间',
                    key: '提交时间'
                },
                {
                    title: '提交结果',
                    key: '提交结果'
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
                                    this.download(params.index)
                                }
                            }
                        }, '下载')
                    }
                },
            ],
            tableData1: [
                {
                    编号: '1000001',
                    提交时间: '2020.01.23',
                    提交结果: 'demo_1.csv',
                }
            ]
        }
    }
}
</script>