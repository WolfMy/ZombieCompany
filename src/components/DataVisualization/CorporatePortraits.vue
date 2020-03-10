<template>
<div class="CorporatePortraits">
    <Breadcrumb style="text-align:left;margin:0px;">
        <BreadcrumbItem>
            数据可视化
        </BreadcrumbItem>
        <BreadcrumbItem>
            <Icon type="ios-reverse-camera" />
            僵尸企业画像
        </BreadcrumbItem>
    </Breadcrumb>
    <Row type="flex" :gutter="16">
        <Col :md="{span:6,order:1}" :xs="{span:24,order:2}" style="margin:16px 0px 0px;">
            <Card dis-hover :padding="16">
                <h2 slot="title" style="text-align:left;">
                    3-1 公司信息
                </h2>
                <template slot="extra">
                    <Tag color="green">著作权</Tag>
                    <Tag color="blue">商标</Tag>
                    <Tag color="geekblue">专利</Tag>
                </template>
                
                <!--CellGroup style="text-align:left;">
                    <Cell title="ID" extra="28" />
                    <Cell title="是否僵尸企业" extra="是" />
                    <Cell title="注册时间" extra="2007" />
                    <Cell title="注册资本" extra="2050万" />
                    <Cell title="控制人类型" extra="企业法人" />
                    <Cell title="区域" extra="福建" />
                    <Cell title="企业类型" extra="农民专业合作社" />
                </CellGroup-->
                <List style="text-align:left;height:400px">
                    <ListItem>
                        <ListItemMeta title="ID" />
                        <template slot="extra">28</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="是否僵尸企业" />
                        <template slot="extra"><Tag color="error">是</Tag></template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="注册时间" />
                        <template slot="extra">2007年</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="注册资本" />
                        <template slot="extra">2050万</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="控制人类型" />
                        <template slot="extra">企业法人</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="区域" />
                        <template slot="extra">福建</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="企业类型" />
                        <template slot="extra">农民专业合作社</template>
                    </ListItem>
                </List>
            </Card>
        </Col>
        <Col :md="{span:10,order:2}" :xs="{span:24,order:3}">
            <Card dis-hover :padding="16" style="margin:16px 0px;">
                <h2 slot="title" style="text-align:left">
                    3-2 TSNE数据可视化
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="描述说明" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo4" style="height:400px;"></div>
            </Card>
        </Col>
        <Col :md="{span:6,offset:2,order:3}" :xs="{span:24,order:1}">
            <Input size="large" search enter-button placeholder="请输入企业ID"  style="margin:16px 0px;">
                <!--Button slot="append" icon="ios-search" -->
            </Input>
        </Col>
    </Row>
    <Card dis-hover :padding="16" style="margin:16px 0px;">
        <h2 slot="title" style="text-align:left">
            3-3 当前企业各指标分布情况
        </h2>
        <Poptip word-wrap width="300" slot="extra" content="展示当前企业在整体企业中的情况。我们分别统计了十五个与僵尸企业强相关的特征在数据集中的平均值，并加入当前企业进行对比。" placement="left">
            <Button size="small" type="info">说明</Button>
        </Poptip>
        <div id="demo3" style="height:550px;"></div>
    </Card>
</div>
</template>
<script>
import Axios from 'axios';
import 'echarts-gl';
export default {
    mounted() {
        this.initCharts()
    },
    methods: {
        initCharts() {
            var color = ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"];
            var myChart3 = this.$echarts.init(document.getElementById('demo3'), 'light');
            var emphasisStyle = {
                // itemStyle: {
                //     barBorderWidth: 1,
                //     shadowBlur: 10,
                //     shadowOffsetX: 0,
                //     shadowOffsetY: 0,
                //     shadowColor: 'rgba(0,0,0,0.5)'
                // }
            };
            var option3 = {
                color: color,
                legend: {
                    data: ['验证集僵尸平均', '验证集非僵尸平均', '训练集僵尸平均', '当前企业'],
                    left: 10
                },
                brush: {
                    toolbox: [''],
                    xAxisIndex: 0
                },
                toolbox: {
                    feature: {
                        magicType: {
                            type: ['stack', 'tiled']
                        },
                        dataView: {}
                    }
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: { // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow', // 默认为直线，可选为：'line' | 'shadow'
                        label: {
                            show: true
                        }
                    },
                    formatter: function (datas) {
                        let res = datas[0].name + '<br/>'
                        let val
                        let length = datas.length
                        let i = 0
                        for (; i < length; i++) {
                            val = datas[i].value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
                            res += '<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:' + datas[i].color + ';"></span>' + datas[i].seriesName + '：' + val + '<br/>'
                        }
                        return res

                    },
                },
                dataZoom: [{
                        show: true,
                        start: 0,
                        end: 100
                    },
                    {
                        type: 'inside',
                        start: 0,
                        end: 100
                    },
                ],
                xAxis: {
                    data: [
                        '2016_纳税总额', '2017_纳税总额', '2015_纳税总额', '2016_主营业务收入', '2016_所有者权益合计',
                        '2017_项目融资和政策融资成本', '2015_主营业务收入', '2016_从业人数', '2017_所有者权益合计',
                        '2016_内部融资和贸易融资成本', '2015_债权融资成本', '2015_所有融资成本之和', '2015_资产总额',
                        '2016_资产负债率', '2015_净利润'
                    ],
                    axisLine: {
                        onZero: true
                    },
                    splitLine: {
                        show: false
                    },
                    splitArea: {
                        show: false
                    }
                },
                yAxis: {
                    inverse: false,
                    splitArea: {
                        show: false
                    },
                    type: "value",
                    axisLabel: {
                        // formatter: function (value, index) {
                        //     return value.toFixed(1);
                        // }
                    },
                },
                grid: {
                    left: 100
                },
                series: [{
                        name: '验证集僵尸平均',
                        type: 'bar',
                        color: color[3],
                        // stack: 'one',
                        data: [832.0375304435472,
                            770.576926999327,
                            672.7664414997747,
                            205217.476342574,
                            -26230.15949378027,
                            65.66034408602148,
                            180059.24255644047,
                            508.7148409596775,
                            -29699.01824103942,
                            1517.0737741935463,
                            232.31777777777768,
                            1785.5464041666664,
                            117823.7032456542,
                            1.2022356630823656,
                            30024.29481906369
                        ],
                    }, {
                        name: '验证集非僵尸平均',
                        type: 'bar',
                        color: color[5],
                        // stack: 'one',
                        data: [115762.3865971159,
                            128716.22649756673,
                            101520.092307396,
                            208342.47732935371,
                            -27707.07507908257,
                            67.03328110767005,
                            182986.2543332105,
                            512.195651473493,
                            -31572.97479686657,
                            1599.9470153944303,
                            235.47314264893387,
                            1811.8559521042207,
                            120123.01527188021,
                            1.2029741300782961,
                            30445.510928996537
                        ],
                    }, {
                        name: '训练集僵尸平均',
                        type: 'bar',
                        // stack: 'one',
                        data: [599.7285219656601,
                            523.0087533274125,
                            411.697381495954,
                            208019.82216202887,
                            -27094.45552063941,
                            68.70551687388989,
                            185715.92840663073,
                            509.7887954405764,
                            -31286.98060407737,
                            1528.152049733569,
                            234.83400828892817,
                            1895.5901120189505,
                            119840.2299555358,
                            1.1789875666074268,
                            31174.492810041487
                        ]
                    }, {
                        name: '当前企业',
                        type: 'bar',
                        // stack: 'one',
                        data: [0.0,
                            0.0,
                            0.0,
                            168336.0,
                            103540.0,
                            0.0,
                            120240.0,
                            977.0,
                            -220440.0,
                            5050.08,
                            0.0,
                            20.04,
                            33400.0,
                            0.48,
                            15030.0,
                            1.0
                        ],
                        color: color[4],
                    },
                    ]
                };
                myChart3.setOption(option3);

                Axios.get("http://120.27.192.52:5555/data/prediction.json").then((res)=>{
                    var myChart4 = this.$echarts.init(document.getElementById('demo4'), "light");
                    var option4 = {
                        color: ["#ff7c7c", "#5bc49f", "#feb64d", "#9287e7"],
                        tooltip: {
                        trigger: "item",
                        },
                        grid3D: {},
                        xAxis3D: {
                        axisLine: {
                        }

                        },
                        yAxis3D: {

                        },
                        zAxis3D: {

                        },
                        legend: {
                        textStyle: {
                            fontSizee: 20
                        },
                        data: ['非僵尸企业', '僵尸企业', '当前企业'],
                        top: 2
                        },
                        series: [{
                        type: 'scatter3D',
                        symbolSize: 4,
                        coordinateSystem: 'cartesian3D',
                        name: "非僵尸企业",
                        data: res.data[1],
                        itemStyle: {
                            color: '#60acfc'
                        },
                        },
                        {
                        type: 'scatter3D',
                        symbolSize: 4,
                        name: "僵尸企业",
                        data: res.data[0],
                        itemStyle: {
                            color: '#ff7c7c'
                        }
                        },
                        {
                        type: 'scatter3D',
                        symbolSize: 12,
                        name: "当前企业",
                        data: [[0.759936092486962, 2.037291155884674, 1.017753063736564]],
                        itemStyle: {
                            color: '#282c34'
                        }
                        }
                        ]
                    };
                    myChart4.setOption(option4);
                });
            }
    }
}
</script>