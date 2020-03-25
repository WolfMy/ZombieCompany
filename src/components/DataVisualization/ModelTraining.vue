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
                        <template slot="extra">CatBoostClassifier</template>
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
        <Col :md="13" :xs="24">
            <Card dis-hover style="margin:16px 0px 0px;">
                <h2 slot="title" style="text-align:left">
                    4-2 
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="描述说明" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo5" style="height:400px;"></div>
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
        <div id="demo1" style="height:400px;"></div>
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
                    }

                },
                legend: {
                    data: ['模型名称', 'Miss_count', 'Accuracy', 'Precision', 'Recall', 'F-measure', 'AUC'],
                },
                xAxis: [
                    {
                    type: 'category',
                    axisTick: {
                        alignWithLabel: true
                    },
                    data: ['CatBoost',
                        'Bagging',
                        'AdaBoost',
                        'Random Forest',
                        'XGBoost',
                        'DTC',
                        'LightGBM',
                        'NN',
                        'LR',
                        'KNN',
                        'NB',
                        'LDA',
                    ],
                    }
                ],
                dataZoom: [
                    {
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
                    },
                ],
                yAxis: [
                    {
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

                    },
                ],
                series: [
                    {
                    name: 'Miss_count',
                    type: 'bar',
                    data: [1, 3, 5, 5, 5, 6, 10, 29, 118, 710, 1163, 1939],
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
                    data: [0.999968, 0.999903, 0.999838, 0.999838, 0.999838, 0.999806, 0.999676, 0.999061, 0.996179, 0.977011, 0.962343, 0.937217,
                    ],

                    },
                    {
                    name: 'Precision',
                    type: 'bar',
                    yAxisIndex: 1,
                    data:
                        [0.9999445, 0.999723, 0.9996675, 0.999866, 0.9998855, 0.9996675, 0.999734, 0.9985715, 0.9937265, 0.9637225, 0.944659, 0.9319155,
                        ],
                    },
                    {
                    name: 'Recall',
                    type: 'bar',
                    yAxisIndex: 1,
                    data: [0.999977, 0.9998855, 0.999863, 0.999899, 0.999723, 0.999863, 0.99971, 0.9987665, 0.997106, 0.9834365, 0.9695605, 0.9144065,
                    ]
                    },
                    {
                    name: 'F1-Score',
                    type: 'bar',
                    yAxisIndex: 1,
                    data:
                        [0.999961, 0.99986, 0.999793, 0.999827, 0.9998045, 0.9997655, 0.9994725, 0.9988075, 0.9953965, 0.9727995, 0.9557575, 0.922557,
                        ]
                    },
                    {
                    name: 'AUC',
                    type: 'bar',
                    yAxisIndex: 1,
                    data:
                        [0.999977, 0.999931, 0.999886, 0.999723, 0.999723, 0.999863, 0.999721, 0.998914, 0.997106, 0.983437, 0.969561, 0.914407],
                    }
                ]
                };
            myChart1.setOption(option1);

            var myChart5 = this.$echarts.init(document.getElementById('demo5'), "light");
            var color = ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"];
            var option5 = {
                color: color,
                toolbox: {
                    show: true,
                    feature: {
                    mark: {
                        show: true
                    },
                    magicType: {
                        show: true,
                        type: ['pie', 'funnel']
                    },
                    }
                },

                "title": {
                    // "text": "南丁格尔玫瑰图--PieHalfRose",
                    // "left": "center",
                    // "top": 20,
                    // "textStyle": {
                    //   "color": "#ccc"
                    // }
                },
                "series": [{
                    "type": "pie",
                    "radius": [
                    30,
                    220
                    ],
                    "avoidLabelOverlap": false,
                    "startAngle": 0,
                    "center": [
                    "50%",
                    "50%"
                    ],
                    "roseType": "area",
                    "selectedMode": "single",
                    "label": {
                    "normal": {
                        "show": true,
                        "formatter": "{b}:{c}",
                        fontSize: 13,
                        fontWeight: 'bolder'
                    },
                    "emphasis": {
                        "show": true
                    }
                    },
                    "labelLine": {
                    "normal": {
                        "show": true,
                        "smooth": false,
                        "length": 12,
                        "length2": 14,
                        lineStyle: {
                        width: 2
                        }
                    },
                    "emphasis": {
                        "show": true
                    }
                    },
                    "data": [{
                    "value": 94.6,
                    "name": "2017-净利润",
                    },
                    {
                    "value": 73.9,
                    "name": "所属行业",
                    },
                    {
                    "value": 62.9,
                    "name": "2016-资产总额",
                    },
                    {
                    "value": 53.8,
                    "name": "2015-净利润",
                    },
                    {
                    "value": 53.3,
                    "name": "2016-净利润",
                    },
                    {
                    "value": 19.0,
                    "name": "控制人持股比例",
                    },
                    {
                    "value": 18.9,
                    "name": "2016-纳税总额",
                    },
                    {
                    "value": 13.1,
                    "name": "2017-债券融资额度",
                    },
                    {
                    "value": 94.6,
                    "name": "2017-净利润",
                    },
                    {
                    "value": 73.9,
                    "name": "所属行业",
                    },
                    {
                    "value": 62.9,
                    "name": "2016-资产总额",
                    },
                    {
                    "value": 53.8,
                    "name": "2015-净利润",
                    },
                    {
                    "value": 53.3,
                    "name": "2016-净利润",
                    },
                    {
                    "value": 19.0,
                    "name": "控制人持股比例",
                    },
                    {
                    "value": 18.9,
                    "name": "2016-纳税总额",
                    },
                    {
                    "value": 13.1,
                    "name": "2017-债券融资额度",
                    }
                ]
            }]
            };
            myChart5.setOption(option5);
        }
    }
}
</script>

<style>

</style>