<template>
<div>
    <div id="demo1" style="width: 600px;height:400px;"></div>
    <div id="demo2" style="width: 600px;height:400px;"></div>
</div>
</template>

<script>
import echarts from 'echarts'
export default {
    data() {
        return {
            myChart1: {},
            myChart2: {},
            dataAxis: [],
            dataShadow: [],
            data1: [],
            hours: [],
            days: [],
            data2: [],
        }
    },
    methods: {
        initCharts() {
            this.myChart1 = echarts.init(document.getElementById('demo1'))
            var zoomSize = 6
            this.myChart1.on('click', (params)=> {
                console.log(this.dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
                this.myChart1.dispatchAction({
                    type: 'dataZoom',
                    startValue: this.dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
                    endValue: this.dataAxis[Math.min(params.dataIndex + zoomSize / 2, this.data1.length - 1)]
                })
            })
            this.myChart1.setOption(
                {
                    title: {
                        text: '每年注册公司数量',
                        subtext: '验证集中2000年到2014年公司注册数量'
                    },
                    xAxis: {
                        data: this.dataAxis,
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
                            textStyle: {
                                color: '#999'
                            }
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
                            data: this.dataShadow,
                            animation: false
                        },
                        {
                            type: 'bar',
                            itemStyle: {
                                color: new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        { offset: 0, color: '#83bff6' },
                                        { offset: 0.5, color: '#188df0' },
                                        { offset: 1, color: '#188df0' }
                                    ]
                                )
                            },
                            emphasis: {
                                itemStyle: {
                                    color: new echarts.graphic.LinearGradient(
                                        0, 0, 0, 1,
                                        [
                                            { offset: 0, color: '#2378f7' },
                                            { offset: 0.7, color: '#2378f7' },
                                            { offset: 1, color: '#83bff6' }
                                        ]
                                    )
                                }
                            },
                            data: this.data1
                        }
                    ]
                }
            )

            this.myChart2 = echarts.init(document.getElementById('demo2'))
            this.myChart2.setOption(
                {
                    tooltip: {
                        position: 'top'
                    },
                    animation: false,
                    grid: {
                        height: '50%',
                        top: '10%'
                    },
                    xAxis: {
                        type: 'category',
                        data: this.hours,
                        splitArea: {
                            show: true
                        }
                    },
                    yAxis: {
                        type: 'category',
                        data: this.days,
                        splitArea: {
                            show: true
                        }
                    },
                    visualMap: {
                        min: 0,
                        max: 10,
                        calculable: true,
                        orient: 'horizontal',
                        left: 'center',
                        bottom: '15%'
                    },
                    series: [{
                        name: 'Punch Card',
                        type: 'heatmap',
                        data: this.data2,
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
                }
            )
        },
        initData1() {
            // 指定图表的配置项和数据
            this.dataAxis = [2000.0, 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0,
                2008.0, 2009.0, 2010.0, 2011.0, 2012.0, 2013.0, 2014.0
            ];
            this.data1 = [2024, 2024, 2063, 2022, 1974, 1980, 2116, 2001, 1971, 2065, 2028, 2021, 2068, 2088, 2122]
            var yMax = 2500;
            for (var i = 0; i < this.data1.length; i++) {
                this.dataShadow.push(yMax);
            }
        },
        initData2() {
            this.hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
                    '7a', '8a', '9a','10a','11a',
                    '12p', '1p', '2p', '3p', '4p', '5p',
                    '6p', '7p', '8p', '9p', '10p', '11p'];
            this.days = ['Saturday', 'Friday', 'Thursday',
                    'Wednesday', 'Tuesday', 'Monday', 'Sunday'];

            this.data2 = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1],[4,0,1],[4,1,3],[4,2,0],[4,3,0],[4,4,0],[4,5,1],[4,6,0],[4,7,0],[4,8,0],[4,9,2],[4,10,4],[4,11,4],[4,12,2],[4,13,4],[4,14,4],[4,15,14],[4,16,12],[4,17,1],[4,18,8],[4,19,5],[4,20,3],[4,21,7],[4,22,3],[4,23,0],[5,0,2],[5,1,1],[5,2,0],[5,3,3],[5,4,0],[5,5,0],[5,6,0],[5,7,0],[5,8,2],[5,9,0],[5,10,4],[5,11,1],[5,12,5],[5,13,10],[5,14,5],[5,15,7],[5,16,11],[5,17,6],[5,18,0],[5,19,5],[5,20,3],[5,21,4],[5,22,2],[5,23,0],[6,0,1],[6,1,0],[6,2,0],[6,3,0],[6,4,0],[6,5,0],[6,6,0],[6,7,0],[6,8,0],[6,9,0],[6,10,1],[6,11,0],[6,12,2],[6,13,1],[6,14,3],[6,15,4],[6,16,0],[6,17,0],[6,18,0],[6,19,0],[6,20,1],[6,21,2],[6,22,2],[6,23,6]];

            this.data2 = this.data2.map(function (item) {
                return [item[1], item[0], item[2] || '-'];
            })
        },
        /*
        handleClick1(params) {
            var zoomSize = 6;
            console.log(params)
            console.log(this.dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
            this.myChart1.dispatchAction({
                type: 'dataZoom',
                startValue: this.dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
                endValue: this.dataAxis[Math.min(params.dataIndex + zoomSize / 2, this.data1.length - 1)]
            });
        }
        */
    },
    mounted() {
        this.initData1()
        this.initData2()
        this.initCharts()
    },
    /*
    watch: {
        option1: {
            handler(newVal, oldVal) {
                if(newVal){
                    this.myChart1.setOption(newVal)
                }else{
                    this.myChart1.setOption(oldVal)
                }
            },
            deep: true
        }
    }
    */
}
</script>
