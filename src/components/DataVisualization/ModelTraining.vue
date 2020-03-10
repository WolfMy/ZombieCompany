<template>
  <div class="ModelTraining">
    <Breadcrumb style="text-align:left;margin:0px;">
        <BreadcrumbItem>
            数据可视化
        </BreadcrumbItem>
        <BreadcrumbItem>
            <Icon type="ios-reverse-camera" />
            模型训练可视化
        </BreadcrumbItem>
    </Breadcrumb>
    <Row type="flex" :gutter="16">
        <Col :md="6" :xs="24">
            <Card dis-hover :padding="16" style="margin:16px 0px 0px;">
                <h2 slot="title" style="text-align:left;">
                    4-1 模型信息
                </h2>
                <List style="text-align:left;height:400px;">
                    <ListItem>
                        <ListItemMeta title="模型名称" />
                        <template slot="extra">28</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="CatBoostClassifier" />
                        <template slot="extra"><Tag color="success">是</Tag></template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="Iterations" />
                        <template slot="extra">1500</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="learning_rate" />
                        <template slot="extra">0.08</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="Depth" />
                        <template slot="extra">7</template>
                    </ListItem>
                </List>
            </Card>
        </Col>
        <Col :md="10" :xs="24">
            <Card dis-hover style="margin:16px 0px 0px;">
                <h2 slot="title" style="text-align:left">
                    4-2 
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="描述说明" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo2" style="height:400px;"></div>
            </Card>
        </Col>
    </Row>
    <Card dis-hover :padding="16" style="margin:16px 0px;">
        <h2 slot="title" style="text-align:left">
            4-3
        </h2>
        <Poptip word-wrap width="300" slot="extra" content="描述说明" placement="left">
            <Button size="small" type="info">说明</Button>
        </Poptip>
        <div id="demo1" style="height:550px;"></div>
    </Card>
</div>
</template>

<script>

export default {
    mounted() {
        this.initCharts()
    },
    methods: {
        initCharts() {
            var myChart1 = this.$echarts.init(document.getElementById('demo1'), "light");
            var option1 = {
                color: ["#ff7c7c", "#5bc49f", "#feb64d", "#9287e7"],
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                grid: {
                    right: '20%'
                },
                toolbox: {
                    feature: {
                        restore: { show: true },
                        magicType: { show: true, type: ['line', 'bar'] },
                        saveAsImage: { show: true }
                    }
                },
                legend: {
                    data: ['模型名称', 'Miss_count', 'Accuracy', 'F-measure', 'AUC'],
                },
                xAxis: [{
                    type: 'category',
                    axisTick: {
                        alignWithLabel: true
                    },
                    data: ['CatBoost', 'Bagging', 'Random Forest', 'AdaBoost', 'DTC', 'LightGBM', 'NN', 'XGBoost', 'LR', 'KNN', 'NB', 'LDA'],
                }],
                dataZoom: [{
                    type: 'slider',
                    show: true,
                    xAxisIndex: 0,
                    start: 0,
                    end: 20,
                    handleSize: 2
                },
                {
                    type: 'inside',
                    start: 0,
                    end: 20
                }],
                yAxis: [{
                    type: 'value',
                    name: '分错个数',
                    min: 0,
                    max: 2500,
                    position: 'left',
                    inverse: false,
                    axisLine: {
                        lineStyle: {
                        // color: colors[0]
                        }
                    },
                    axisLabel: {
                        formatter: '{value} 个'
                    }
                },
                {
                    type: 'value',
                    name: '准确率',
                    min: 0.999,
                    max: 1.0,
                    position: 'right',
                    axisLine: {
                        lineStyle: {
                        // color: colors[1]
                        }
                    },
                    axisLabel: {
                        formatter: '{value}'
                    },

                }],
                series: [{
                    name: 'Miss_count',
                    type: 'bar',
                    data: [1, 3, 5, 5, 6, 10, 29, 98, 118, 710, 1163, 1939],
                    yAxisIndex: 0,
                    markPoint: {
                        data: [
                        { type: 'max', name: '最大值' },
                        { type: 'min', name: '最小值' }
                        ]
                    },
                },
                {
                    name: 'Accuracy',
                    type: 'bar',
                    yAxisIndex: 1,
                    data: [0.999968, 0.999903, 0.999838, 0.999838, 0.999806, 0.999676, 0.999061, 0.996827, 0.996179, 0.977011, 0.962343, 0.937217],
                },
                {
                    name: 'F-measure',
                    type: 'bar',
                    yAxisIndex: 1,
                    data: [0.999977, 0.999834, 0.999723, 0.999723, 0.999668, 0.999533, 0.998393, 0.994542, 0.993498, 0.962097, 0.938689, 0.888863],
                },
                {
                    name: 'AUC',
                    type: 'bar',
                    yAxisIndex: 1,
                    data: [0.999945, 0.999931, 0.999723, 0.999886, 0.999863, 0.999721, 0.998914, 0.997768, 0.997106, 0.983437, 0.969561, 0.914407],
                }]
            };
            myChart1.setOption(option1);

            var myChart2 = this.$echarts.init(document.getElementById('demo2'), "light");
            var option2 = {
            tooltip: {},
            xAxis: {
                type: 'value',
                data: [5000, 10000, 15000, 20000, 25000],

            },
            legend: {

            },
            grid: {
            },
            yAxis: {
                type: 'value',
                min: 0.2,
                max: 1.0
            },
            series: [{
                name: "训练集",
                data: [[2779, 0.99830874], [9033, 0.99227278], [15287, 0.99532936], [21541, 0.99661111], [27795, 0.99740601]],
                type: 'line'
            },
            {
                name: "测试集",
                data: [[2779, 0.28908172], [9033, 0.99585544], [15287, 0.99663254], [21541, 0.99679443], [27795, 0.99689158]],
                type: 'line',
                itemStyle: {
                color: '#ff7c7c'
                }
            }
            ]
            };
            myChart2.setOption(option2);
        }
    }
}
</script>

<style>

</style>