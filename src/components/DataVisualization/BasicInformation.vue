<template>
<div class="BasicInformation">
    <Breadcrumb style="text-align:left;margin:0px;">
        <BreadcrumbItem>
            数据可视化展示
        </BreadcrumbItem>
        <BreadcrumbItem>
            <Icon type="ios-information-circle-outline" />
            数据分布可视化
        </BreadcrumbItem>
    </Breadcrumb>
    <Row :gutter="16" style="margin:0px -16px;">
        <Col :md="14" :xs="24" style="margin:16px 0px;">
            <Card dis-hover :padding="8">
                <h2 slot="title" style="text-align:left">
                    1-1 缺失值数量
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="验证集所给出的四个表中各特征的缺失情况，可以看到除企业ID外均出现一定程度数据缺失的情况。对于数据的缺失，我们将根据不同数据自身的特性，使用合适方法进行填充。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo1" style="height:500px;"></div>
            </Card>
        </Col>
        <Col :md="10" :xs="24" style="margin:16px 0px;">
            <Card dis-hover :padding="8">
                <h2 slot="title" style="text-align:left">
                    1-2 僵尸企业分布
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="展示了验证集所提供数据中，僵尸企业在中国地图上的数量和分布情况。个省份僵尸企业数量集中在1200-1300之间，数量差异较小。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo3" style="height:500px;"></div>
            </Card>
        </Col>
    </Row>
    <Row :gutter="16" style="margin:0px -16px;">
        <Col :md="8" :xs="24" style="margin:16px 0px;">
            <Card dis-hover style="text-align:left" :padding="24">
                <h2 slot="title">
                    1-3 每年注册公司数量
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="展示了验证集提供的企业数据中，从2000年到2014年每年的公司注册数量。可以看到每年的注册数量比较平均，在2000家附近小幅度波动。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo4" style="height:400px;"></div>
            </Card>
        </Col>
        <Col :md="16" :xs="24" style="margin:16px 0px;">
            <Card dis-hover style="text-align:left" :padding="24">
                <h2 slot="title">
                    1-4 各特征企业数量占比
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="展示了验证集提供的基本信息表中企业所属行业、企业类型、控制人类型、所在区域四个特征中各类别数量占比情况。可以看到各个特征中各自的类别数量占比情况比较均匀。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo2" style="height:400px;"></div>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>
import 'echarts/map/js/china'
export default {
    mounted() {
        this.initCharts()
    },
    methods: {
        initCharts() {
            var myChart1 = this.$echarts.init(document.getElementById('demo1'), "light");
            var sizeValue = '53%';
            var symbolSize = 2.5;
            var color = ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"];
            var option1 = {
                // backgroundColor: '#f7f7f7',
                //  color: ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"],
                color: color,
                tooltip: {
                    trigger: 'axis',
                    axisPointer: { // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                legend: {},
                grid: [{
                        right: sizeValue,
                        bottom: sizeValue
                    },
                    {
                        left: sizeValue,
                        bottom: sizeValue
                    },
                    {
                        right: sizeValue,
                        top: sizeValue
                    },
                    {
                        left: sizeValue,
                        top: sizeValue
                    }
                ],
                xAxis: [{
                    type: 'category',
                    gridIndex: 0,
                    data: ['ID', '注册时间', '注册资本', '行业', '区域', '企业类型', '控制人类型', '控制人ID', '控制人持股比例', 'flag'],
                    axisTick: {
                        alignWithLabel: true
                    },
                }, {
                    type: 'category',
                    gridIndex: 1,
                    data: ['债权融资额度', '债权融资成本', '股权融资额度', '股权融资成本', '内部融资和贸易融资额度', '内部融资和贸易融资成本', '项目融资和政策融资额度', '项目融资和政策融资成本'],
                    axisTick: {
                        alignWithLabel: true
                    },
                }, {
                    type: 'category',
                    gridIndex: 2,
                    data: ['从业人数', '资产总额', '负债总额', '营业总收入', '主营业务收入', '利润总额', '净利润', '纳税总额', '所有者权益合计'],
                    axisTick: {
                        alignWithLabel: true
                    },
                }, {
                    type: 'category',
                    gridIndex: 3,
                    data: ['专利', '商标', '著作权'],
                    axisTick: {
                        alignWithLabel: true
                    },
                }],
                yAxis: [{
                    type: 'value',
                    gridIndex: 0
                }, {
                    type: 'value',
                    gridIndex: 1,
                }, {
                    type: 'value',
                    gridIndex: 2,
                }, {
                    type: 'value',
                    gridIndex: 3
                }],
                series: [{
                        name: 'baseInfo',
                        type: 'bar',
                        xAxisIndex: 0,
                        yAxisIndex: 0,
                        barWidth: '70%',
                        data: [0, 317, 323, 277, 285, 317, 339, 282, 315, 306],
                    },
                    {
                        name: 'moneyReport',
                        type: 'bar',
                        xAxisIndex: 1,
                        yAxisIndex: 1,
                        data: [891, 962, 925, 943, 862, 902, 953, 932],
                    },
                    {
                        name: 'yearReport',
                        type: 'bar',
                        xAxisIndex: 2,
                        yAxisIndex: 2,
                        data: [897, 994, 875, 933, 907, 902, 949, 898, 955],
                    },
                    {
                        name: 'knowledge',
                        type: 'bar',
                        xAxisIndex: 3,
                        yAxisIndex: 3,
                        barWidth: '30%',
                        data: [308, 319, 296],
                    }

                ]
            };
            myChart1.setOption(option1);

            var myChart2 = this.$echarts.init(document.getElementById('demo2'), "light");
            var option2 = {
                color: color,
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: [{
                    type: 'scroll',
                    orient: 'vertical',
                    name: '行业数量占比',
                    data: ['交通运输业', '商业服务业', '工业', '服务业', '社区服务', '零售业'],
                    selected: ['交通运输业', '商业服务业', '工业', '服务业', '社区服务', '零售业'],
                    left: 'left',
                }, {
                    show: true,
                    name: '控制人类型比例',
                    type: 'scroll',
                    orient: 'vertical',
                    data: ['企业法人', '自然人'],
                    selected: ['企业法人', '自然人'],
                    left: 'left',
                    top: 'center'
                }, {
                    type: 'scroll',
                    orient: 'vertical',
                    show: true,
                    data: ['农民专业合作社', '合伙企业', '有限责任公司', '股份有限公司', '集体所有制企业'],
                    selected: ['农民专业合作社', '合伙企业', '有限责任公司', '股份有限公司', '集体所有制企业'],
                    left: 'right',
                }, {
                    type: 'scroll',
                    orient: 'vertical',
                    data: ['山东', '广东', '广西', '江西', '湖北', '湖南', '福建'],
                    selected: ['山东', '广东', '广西', '江西', '湖北', '湖南', '福建'],
                    left: 'right',
                    top: '40%'
                }],
                series: [{
                        name: '行业数量占比',
                        type: 'pie',
                        radius: '29%',
                        center: ['30%', '25%'],
                        data: [{
                            'name': '交通运输业',
                            'value': 5272
                        }, {
                            'name': '商业服务业',
                            'value': 5158
                        }, {
                            'name': '工业',
                            'value': 5112
                        }, {
                            'name': '服务业',
                            'value': 5151
                        }, {
                            'name': '社区服务',
                            'value': 5087
                        }, {
                            'name': '零售业',
                            'value': 5104
                        }],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },
                    },
                    {
                        name: '控制人类型比例',
                        type: 'pie',
                        radius: '29%',
                        center: ['30%', '75%'],
                        data: [{
                            'name': '企业法人',
                            'value': 15591
                        }, {
                            'name': '自然人',
                            'value': 15293
                        }],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },

                    },
                    {
                        name: '企业类型比例',
                        type: 'pie',
                        radius: '29%',
                        center: ['70%', '25%'],
                        data: [{
                            'name': '农民专业合作社',
                            'value': 6131
                        }, {
                            'name': '合伙企业',
                            'value': 6273
                        }, {
                            'name': '有限责任公司',
                            'value': 6152
                        }, {
                            'name': '股份有限公司',
                            'value': 6131
                        }, {
                            'name': '集体所有制企业',
                            'value': 6197
                        }],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },
                    },
                    {
                        name: '区域比例',
                        type: 'pie',
                        radius: '29%',
                        center: ['70%', '75%'],
                        data: [{
                            'name': '山东',
                            'value': 4387
                        }, {
                            'name': '广东',
                            'value': 4420
                        }, {
                            'name': '广西',
                            'value': 4444
                        }, {
                            'name': '江西',
                            'value': 4466
                        }, {
                            'name': '湖北',
                            'value': 4386
                        }, {
                            'name': '湖南',
                            'value': 4397
                        }, {
                            'name': '福建',
                            'value': 4384
                        }],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        },
                    }
                ]
            };
            myChart2.setOption(option2);

            var myChart3 = this.$echarts.init(document.getElementById('demo3'), "light");
            var data3 = [
                {
                    'name': '山东',
                    'value': 1271
                },
                {
                    'name': '广东',
                    'value': 1258
                },
                {
                    'name': '广西',
                    'value': 1294
                },
                {
                    'name': '江西',
                    'value': 1304
                },
                {
                    'name': '湖北',
                    'value': 1245
                },
                {
                    'name': '湖南',
                    'value': 1266
                },
                {
                    'name': '福建',
                    'value': 1290
                }
            ]
            var option3 = {
                color: ["#5bc49f", "#feb64d", "#9287e7", "#ff7c7c"],
                grid: {
                    right: 10,
                    top: 135,
                    bottom: 100,
                    width: '20%'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}<br/>数量: {c}'
                },
                visualMap: {
                    seriesIndex: 0,
                    min: 1200,
                    max: 1300,
                    left: 'left',
                    top: 'bottom',
                    text: ['高', '低'],
                    calculable: true,
                },
                series: [{
                    zlevel: 1,
                    name: '中国僵尸企业分布',
                    type: 'map',
                    mapType: 'china',
                    selectedMode: 'multiple',
                    roam: "move",
                    scaleLimit: {
                    min: 0.5,
                    max: 0.85,
                    },
                    zoom: 0.75,
                    left: 0,
                    right: '10%',
                    label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                    },
                    data: data3
                },]
            };
            myChart3.setOption(option3);

            // 基于准备好的dom，初始化echarts实例
            var myChart4 = this.$echarts.init(document.getElementById('demo4'));
            // 指定图表的配置项和数据
            var dataAxis = [2000.0, 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0,
                2008.0, 2009.0, 2010.0, 2011.0, 2012.0, 2013.0, 2014.0
            ];
            var data = [2024, 2024, 2063, 2022, 1974, 1980, 2116, 2001, 1971, 2065, 2028, 2021, 2068, 2088, 2122]
            var yMax = 2500;
            var dataShadow = [];
            for (var i = 0; i < data.length; i++) {
                dataShadow.push(yMax);
            }
            var option4 = {
                color: color,
                xAxis: {
                    data: dataAxis,
                    axisLabel: {
                        inside: true,
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    z: 10
                },
                yAxis: {
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                    }
                },
                dataZoom: [{
                    type: 'inside'
                }],
                series: [{ // For shadow
                        type: 'bar',
                        itemStyle: {
                            color: 'rgba(0,0,0,0.05)'
                        },
                        barGap: '-100%',
                        barCategoryGap: '40%',
                        data: dataShadow,
                        animation: false
                    },
                    {
                        type: 'bar',
                        data: data
                    }
                ]
            };
            // Enable data zoom when user click bar.
            var zoomSize = 6;
            myChart1.on('click', function (params) {
                console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
                myChart1.dispatchAction({
                    type: 'dataZoom',
                    startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
                    endValue: dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
                });
            });
            // 使用刚指定的配置项和数据显示图表。
            myChart4.setOption(option4);
        }
    }
}
</script>