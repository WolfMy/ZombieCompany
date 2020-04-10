<template>
<div class="RelevanceExplore">
    <Breadcrumb style="text-align:left;margin:0px;">
        <BreadcrumbItem>
            数据可视化
        </BreadcrumbItem>
        <BreadcrumbItem>
            <Icon type="ios-analytics" />
            数据关联性探索
        </BreadcrumbItem>
    </Breadcrumb>
    <Row :gutter="16" type="flex" align="middle" style="margin:0px -16px;">
        <Col :md="15" :xs="24" style="margin:16px 0px;">
            <Card dis-hover>
                <h2 slot="title" style="text-align:left">
                    2-1 注册时间与僵尸企业的关联
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="探索了“注册时间”与“能否成为僵尸企业”之间的关系。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo1" style="height:400px;"></div>
            </Card>
        </Col>
        <Col :md="9" :xs="24" style="margin:16px 0px;">
            <Card dis-hover>
                <h2 slot="title" style="text-align:left">
                    2-2 知识产权数量与僵尸企业的关联
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="探索“知识产权相关的特征”与“能否成为僵尸企业”之间的关系。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo4" style="height:400px;"></div>
            </Card>
        </Col>
    </Row>
    <Row :gutter="16"  type="flex" align="middle" style="margin:0px -16px;">
        <Col :md="10" :xs="24" style="margin:16px 0px;">
            <Card dis-hover>
                <h2 slot="title" style="text-align:left">
                    2-3 企业三年纳税总额
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="探索了“企业三年纳税情况”与“是否被认为是僵尸企业”的相关性。将三年纳税的数量直接对应三维坐标轴上的值，僵尸企业与非僵尸企业的数据分布呈现明显不同。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo2" style="height:500px;"></div>
            </Card>
        </Col>
        <Col :md="14" :xs="24" style="margin:16px 0px;">
            <Card dis-hover>
                <h2 slot="title" style="text-align:left">
                    2-4 各特征与僵尸企业的关联
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="探究验证集中企业基本信息表各特征与“是否被认为是僵尸企业”之间的相关性。可以看到各维度下的各种分类占比都比较均匀，僵尸企业和非僵尸企业下数据的分布没有明显的差异性。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo3" style="height:500px;"></div>
            </Card>
        </Col>
    </Row>
    <Row style="margin:0px -10px;">
        <Col span="24">
            <Card dis-hover>
                <h2 slot="title" style="text-align:left">
                    2-5 年报表各特征相关性分析
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="展示了验证集中年报（year_report）表中各特征之间的皮尔逊系数热力图。绝对值越大、颜色越深表示相关性越高，其中1表示完全正相关，-1表示完全负相关。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo5" style="height:500px;"></div>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>
import Axios from 'axios'
import 'echarts-gl' 
export default {
    mounted() {
        this.initCharts()
    },
    methods: {
        initCharts() {
            var myChart1 = this.$echarts.init(document.getElementById('demo1'), "light");
            var color = ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"];

            var xData = function () {
                var data = [];
                for (var i = 2000; i <= 2014; i++) {
                    data.push(i + "年");
                }
                return data;
            }();

            var option1 = {
                color: color,
                backgroundColor: "#fff",
                "tooltip": {
                    "trigger": "axis",
                    "axisPointer": {
                        "type": "shadow",
                    },
                },
                "grid": {
                    "borderWidth": 0,
                },
                "legend": {
                    "data": ['僵尸企业', '非僵尸企业', '平均']
                },
                "calculable": true,
                "xAxis": [{
                    "type": "category",
                    "axisLine": {},
                    "data": xData,
                }],
                "yAxis": [{
                    "type": "value",
                }],
                "dataZoom": [{
                    "show": true,
                    "height": 30,
                    "xAxisIndex": [
                        0
                    ],
                    "start": 10,
                    "end": 80,
                    handleSize: '110%',
                }],
                "series": [{
                        "name": "僵尸企业",
                        "type": "bar",
                        "stack": "总量",
                        "barMaxWidth": 35,
                        "barGap": "10%",
                        "itemStyle": {
                            "normal": {
                                "color": "#5BC49F",
                                "label": {
                                    "show": true,
                                    "position": "inside",
                                    formatter: function (p) {
                                        return p.value > 0 ? (p.value) : '';
                                    }
                                }
                            }
                        },
                        "data": [
                            605, 603, 569, 592, 539, 573, 619, 592, 583, 610, 616, 590, 609, 622, 606
                        ],
                    },

                    {
                        "name": "非僵尸企业",
                        "type": "bar",
                        "stack": "总量",
                        "itemStyle": {
                            "normal": {
                                "color": "#60ACFC",
                                "barBorderRadius": 0,
                                "label": {
                                    "show": true,
                                    "position": "inside",
                                    formatter: function (p) {
                                        return p.value > 0 ? (p.value) : '';
                                    }
                                }
                            }
                        },
                        "data": [
                            1411, 1426, 1427, 1441, 1443, 1450, 1453, 1458, 1475, 1484, 1486, 1507,
                            1522, 1546, 1546
                        ],
                    }, {
                        "name": "总数",
                        "type": "line",
                        symbolSize: 10,
                        symbol: 'circle',
                        "itemStyle": {
                            "normal": {
                                "color": "#FF7C7C",
                                "barBorderRadius": 0,
                                "label": {
                                    "show": true,
                                    "position": "top",
                                    formatter: function (p) {
                                        return p.value > 0 ? (p.value) : '';
                                    }
                                }
                            }
                        },
                        "data": [
                            2046,
                            2046,
                            2076,
                            2050,
                            1989,
                            2000,
                            2141,
                            2018,
                            1994,
                            2094,
                            2043,
                            2043,
                            2084,
                            2108,
                            2152
                        ]
                    },
                ],

            }

            myChart1.setOption(option1);

            Axios.get("http://cdn.zomboost.dcts.top/demo6.json").then((res)=>{
                var myChart2 = this.$echarts.init(document.getElementById('demo2'), "light");
                var option2 = {
                    color: color,
                    tooltip: {
                        trigger: "item",
                    },
                    grid3D: {},
                    xAxis3D: {
                        name: "2015年纳税总额",
                        nameGap: 35,
                        type: 'value',
                        axisPointer: {
                            show: false,
                        },
                    },
                    yAxis3D: {
                        name: "2016年纳税总额",
                        nameGap: 35,
                        type: 'value',
                        axisPointer: {
                            show: false,
                        },
                    },
                    zAxis3D: {
                        name: "2017年纳税总额",
                        nameGap: 35,
                        type: 'value',
                        axisPointer: {
                            show: false,
                        },
                    },
                    legend: {
                        textStyle: {
                            fontSizee: 20
                        },
                        data: ['非僵尸企业', '僵尸企业'],
                        top: 2
                    },
                    series: [{
                        type: 'scatter3D',
                        symbolSize: 4,
                        coordinateSystem: 'cartesian3D',
                        name: "非僵尸企业",
                        data: res.data[0],
                        itemStyle: {
                            color: '#60acfc'
                        },
                    },
                    {
                        type: 'scatter3D',
                        symbolSize: 5,
                        name: "僵尸企业",
                        data: res.data[1],
                        itemStyle: {
                            color: '#ff7c7c'
                        }
                    }
                    ]
                };
                myChart2.setOption(option2);
            });



            var myChart3 = this.$echarts.init(document.getElementById('demo3'), "light");

            var dataset = {
                '山东': [1271, 3116],
                '广东': [1258, 3162],
                '广西': [1294, 3150],
                '江西': [1304, 3162],
                '湖北': [1245, 3141],
                '湖南': [1266, 3131],
                '福建': [1290, 3094],
                '农民专业合作社': [1800, 4331],
                '合伙企业': [1745, 4528],
                '有限责任公司': [1841, 4311],
                '股份有限公司': [1768, 4363],
                '集体所有制企业': [1774, 4423],
                '企业法人': [4562, 11029],
                '自然人': [4366, 10927],
                '交通运输业': [1590, 3682],
                '商业服务业': [1480, 3678],
                '工业': [1493, 3619],
                '服务业': [1469, 3682],
                '社区服务': [1449, 3638],
                '零售业': [1447, 3657]
            };
            var option3 = {
                color: color,
                tooltip: {
                    trigger: 'axis',
                    axisPointer: { // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                legend: {
                    type: 'scroll',
                    left: 'right',
                    data: ['山东', '广东', '广西', '江西', '湖北', '湖南', '福建', '农民专业合作社', '合伙企业', '有限责任公司', '股份有限公司', '集体所有制企业', '企业法人', '自然人', '交通运输业', '商业服务业', '工业', '服务业', '社区服务', '零售业'],
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: [{
                    type: 'category',
                    data: ['僵尸企业', '非僵尸企业']
                }],
                yAxis: [{
                    type: 'value'
                }],
                series: [{
                        name: '山东',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['山东']
                    }, {
                        name: '广东',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['广东']
                    },
                    {
                        name: '广西',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['广西']
                    },
                    {
                        name: '江西',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['江西']
                    },
                    {
                        name: '湖北',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['湖北']
                    }, {
                        name: '湖南',
                        type: 'bar',
                        stack: '地区',
                        data: dataset['湖南']
                    }, {
                        name: '福建',
                        type: 'bar',
                        stack: '地区',
                        label: {
                            show: true,
                            position: "top",
                            formatter: '地区'
                        },
                        data: dataset['福建']
                    }, {
                        name: '农民专业合作社',
                        type: 'bar',
                        stack: '企业类型',
                        data: dataset['农民专业合作社']
                    }, {
                        name: '合伙企业',
                        type: 'bar',
                        stack: '企业类型',
                        data: dataset['合伙企业']
                    }, {
                        name: '有限责任公司',
                        type: 'bar',
                        stack: '企业类型',
                        data: dataset['有限责任公司']
                    }, {
                        name: '股份有限公司',
                        type: 'bar',
                        stack: '企业类型',
                        data: dataset['股份有限公司']
                    }, {
                        name: '集体所有制企业',
                        type: 'bar',
                        stack: '企业类型',
                        data: dataset['集体所有制企业'],
                        label: {
                            show: true,
                            position: "top",
                            formatter: '企业类型'
                        },
                    }, {
                        name: '企业法人',
                        type: 'bar',
                        stack: '控制人类型',
                        data: dataset['企业法人']
                    },
                    {
                        name: '自然人',
                        type: 'bar',
                        stack: '控制人类型',
                        data: dataset['自然人'],
                        label: {
                            show: true,
                            position: "top",
                            formatter: '控制人类型'
                        },
                    }, {
                        name: '交通运输业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['交通运输业']
                    }, {
                        name: '商业服务业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['商业服务业']
                    }, {
                        name: '工业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['工业']
                    }, {
                        name: '服务业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['服务业']
                    }, {
                        name: '社区服务业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['社区服务业']
                    }, {
                        name: '零售业',
                        type: 'bar',
                        stack: '行业',
                        data: dataset['零售业'],
                        label: {
                            show: true,
                            position: "top",
                            formatter: '行业',

                        },
                    },

                ]
            };
            myChart3.setOption(option3);


            var myChart4 = this.$echarts.init(document.getElementById('demo4'), 'light');

            var option4 = {
                tooltip: {},
                color: color,
                legend: {
                    selected: {
                        '验证集僵尸企业': true, 
                        '验证集非僵尸企业': false, 
                        '训练集僵尸企业': false
                    },
                    data: ['验证集僵尸企业', '验证集非僵尸企业', '训练集僵尸企业']
                },
                radar: {
                    center: ['50 %', '60 %'],
                    indicator: [{
                            text: '有著作权',
                            max: 45,
                        },
                        {
                            name: '有商标',
                            max: 45,
                            axisLabel:{show:true}
                        },
                        {
                            name: '有专利',
                            max: 45
                        },
                        {
                            name: '三项中有一项',
                            max: 15,
                            axisLabel:{show:true}
                        },
                        {
                            name: '三项都有',
                            max: 15
                        },
                    ]
                },
                series: [{
                    name: '',
                    type: 'radar',
                    // areaStyle: {normal: {}},
                    data: [{
                            value: [35.81, 36.1, 33.51, 7.91, 7.91],
                            name: '验证集僵尸企业',
                            areaStyle: {
                                color: color[5],
                            },
                        },
                        {
                            value: [37.53, 36.2, 34.18, 8.38, 8.38],
                            name: '验证集非僵尸企业',
                            areaStyle: {},
                        },
                        {
                            value: [36.41, 34.73, 34.06, 8.05, 8.05],
                            name: '训练集僵尸企业',
                            areaStyle: {},
                        }
                    ]
                }]
            };
            myChart4.setOption(option4);


            var myChart5 = this.$echarts.init(document.getElementById('demo5'), 'light');
            var x = ['从业人数', '资产总额', '负债总额', '营业总收入', '主营业务收入', '利润总额', '净利润', '纳税总额',
                '所有者权益合计', 'flag'
            ];
            var y = ['从业人数', '资产总额', '负债总额', '营业总收入', '主营业务收入', '利润总额', '净利润', '纳税总额',
                '所有者权益合计', 'flag'
            ];

            var data = [
                [0, 0, 1.0],
                [0, 1, -0.012],
                [0, 2, -0.01],
                [0, 3, -0.01],
                [0, 4, -0.008],
                [0, 5, -0.008],
                [0, 6, -0.01],
                [0, 7, -0.003],
                [0, 8, 0.001],
                [0, 9, -0.006],
                [1, 0, -0.012],
                [1, 1, 1.0],
                [1, 2, 0.917],
                [1, 3, 0.877],
                [1, 4, 0.855],
                [1, 5, 0.796],
                [1, 6, 0.877],
                [1, 7, 0.579],
                [1, 8, -0.395],
                [1, 9, -0.012],
                [2, 0, -0.01],
                [2, 1, 0.917],
                [2, 2, 1.0],
                [2, 3, 0.808],
                [2, 4, 0.787],
                [2, 5, 0.736],
                [2, 6, 0.808],
                [2, 7, 0.539],
                [2, 8, -0.717],
                [2, 9, -0.015],
                [3, 0, -0.01],
                [3, 1, 0.877],
                [3, 2, 0.808],
                [3, 3, 1.0],
                [3, 4, 0.969],
                [3, 5, 0.905],
                [3, 6, 1.0],
                [3, 7, 0.656],
                [3, 8, -0.346],
                [3, 9, -0.01],
                [4, 0, -0.008],
                [4, 1, 0.855],
                [4, 2, 0.787],
                [4, 3, 0.969],
                [4, 4, 1.0],
                [4, 5, 0.883],
                [4, 6, 0.969],
                [4, 7, 0.641],
                [4, 8, -0.337],
                [4, 9, -0.011],
                [5, 0, -0.008],
                [5, 1, 0.796],
                [5, 2, 0.736],
                [5, 3, 0.905],
                [5, 4, 0.883],
                [5, 5, 1.0],
                [5, 6, 0.905],
                [5, 7, 0.595],
                [5, 8, -0.319],
                [5, 9, -0.008],
                [6, 0, -0.01],
                [6, 1, 0.877],
                [6, 2, 0.808],
                [6, 3, 1.0],
                [6, 4, 0.969],
                [6, 5, 0.905],
                [6, 6, 1.0],
                [6, 7, 0.656],
                [6, 8, -0.346],
                [6, 9, -0.01],
                [7, 0, -0.003],
                [7, 1, 0.579],
                [7, 2, 0.539],
                [7, 3, 0.656],
                [7, 4, 0.641],
                [7, 5, 0.595],
                [7, 6, 0.656],
                [7, 7, 1.0],
                [7, 8, -0.242],
                [7, 9, -0.422],
                [8, 0, 0.001],
                [8, 1, -0.395],
                [8, 2, -0.717],
                [8, 3, -0.346],
                [8, 4, -0.337],
                [8, 5, -0.319],
                [8, 6, -0.346],
                [8, 7, -0.242],
                [8, 8, 1.0],
                [8, 9, 0.014],
                [9, 0, -0.006],
                [9, 1, -0.012],
                [9, 2, -0.015],
                [9, 3, -0.01],
                [9, 4, -0.011],
                [9, 5, -0.008],
                [9, 6, -0.01],
                [9, 7, -0.422],
                [9, 8, 0.014],
                [9, 9, 1.0]
            ]

            var option5 = {
                colot: color,
                tooltip: {
                    position: 'top'
                },
                animation: false,
                grid: {
                    top: 10,
                    bottom: '20%'
                },
                xAxis: {
                    type: 'category',
                    data: x,
                    splitArea: {
                        show: true
                    }
                },
                yAxis: {
                    type: 'category',
                    data: y,
                    splitArea: {
                        show: true
                    }
                },
                visualMap: {
                    min: -1,
                    max: 1,
                    calculable: true,
                    orient: 'horizontal',
                    left: 'center',
                    bottom: 5,
                    // inRange: {
                    //     color: ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196027']
                    // },
                },
                series: [{
                    name: 'Punch Card',
                    type: 'heatmap',
                    data: data,
                    label: {
                        show: true
                    },
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }]
            };
            myChart5.setOption(option5);
        }
    }
}
</script>