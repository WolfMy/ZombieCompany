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
                <!--template slot="extra">
                    <Tag color="green">著作权</Tag>
                    <Tag color="blue">商标</Tag>
                    <Tag color="geekblue">专利</Tag>
                </template-->
                <List style="text-align:left;height:400px">
                    <ListItem>
                        <ListItemMeta title="ID" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['ID']}}</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="是否僵尸企业" />
                        <template slot="extra">
                            <Tag color="error" v-if="this.companyInfo[this.currentID]['isZombie']=='是'">是</Tag>
                            <Tag color="success" v-else>否</Tag>
                        </template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="注册时间" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['registerTime']}}年</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="注册资本" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['registerMoney']}}万</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="控制人类型" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['controlType']}}</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="区域" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['area']}}</template>
                    </ListItem>
                    <ListItem>
                        <ListItemMeta title="企业类型" />
                        <template slot="extra">{{this.companyInfo[this.currentID]['companyType']}}</template>
                    </ListItem>
                </List>
            </Card>
        </Col>
        <Col :md="{span:10,order:2}" :xs="{span:24,order:3}">
            <Card dis-hover :padding="16" style="margin:16px 0px;">
                <h2 slot="title" style="text-align:left">
                    3-2 TSNE数据可视化
                </h2>
                <Poptip word-wrap width="300" slot="extra" content="通过TSNE工具将高维数据降到三维后，用可视化的方式定性分析僵尸企业和非僵尸企业的分布情况。" placement="left">
                    <Button size="small" type="info">说明</Button>
                </Poptip>
                <div id="demo4" style="height:400px;"></div>
            </Card>
        </Col>
        <Col :md="{span:8,order:3}" :xs="{span:24,order:1}">
            <Row :gutter="0">
                <Col :span="20">
                <Input size="large" @on-search="searchID" search enter-button placeholder="请输入企业ID"  style="margin:16px 0px;" />
                </Col>
                <Col :span="4">
                <Poptip word-wrap width="300" content="考虑系统性能，平台选取较有代表性样例展示，后期根据应用进行拓展。目前提供ID有：1500001、1500321、1507545、2932443、3356449、5978041、5978042、5978081、5978099、5988104。" placement="left" style="margin:16px 0px;">
                    <Button size="large" type="success">说明</Button>
                </Poptip>
                </Col>
            </Row>
            <Row>
                <Card dis-hover :padding="16">
                    <h2 slot="title" style="text-align:left">
                        3-3 企业知识产权统计
                    </h2>
                    <Poptip word-wrap width="300" slot="extra" content="统计了当前企业专利、商标、著作权的数量情况。" placement="left">
                        <Button size="small" type="info">说明</Button>
                    </Poptip>
                    <div id="demo1" style="height:345px;"></div>
                </Card>
            </Row>
        </Col>
    </Row>
    <Card dis-hover :padding="16" style="margin:16px 0px;">
        <h2 slot="title" style="text-align:left">
            3-4 当前企业各指标分布情况
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
    data() {
        return {
            currentID: 1500001,
            companyInfo: {
                1500001:{ '专利': 0, '商标': 0, '著作权': 0, 'ID': 1500001, 'isZombie': '是', 'registerTime': 2010, 'registerMoney': '6680', 'controlType': '自然人', 'area': '山东', 'companyType': '股份有限公司' },
                1500321:{ '专利': 0, '商标': 0, '著作权': 0, 'ID': 1500321, 'isZombie': '是', 'registerTime': 2001, 'registerMoney': '9330', 'controlType': '企业法人', 'area': '广东', 'companyType': '股份有限公司' },
                1507545:{ '专利': 1, '商标': 1, '著作权': 1, 'ID': 1507545, 'isZombie': '是', 'registerTime': 2000, 'registerMoney': '3840', 'controlType': '企业法人', 'area': '山东', 'companyType': '有限责任公司' },
                2932443:{ '专利': 0, '商标': 0, '著作权': 1, 'ID': 2932443, 'isZombie': '是', 'registerTime': 2014, 'registerMoney': '4600', 'controlType': '企业法人', 'area': '广西', 'companyType': '集体所有制企业' },
                3356449:{ '专利': 0, '商标': 1, '著作权': 1, 'ID': 3356449, 'isZombie': '是', 'registerTime': 2009, 'registerMoney': '8760', 'controlType': '企业法人', 'area': '湖南', 'companyType': '农民专业合作社' },
                5978041:{ '专利': 1, '商标': 1, '著作权': 0, 'ID': 5978041, 'isZombie': '否', 'registerTime': 2005, 'registerMoney': '3500', 'controlType': '企业法人', 'area': '山东', 'companyType': '有限责任公司' },
                5978042:{ '专利': 0, '商标': 0, '著作权': 0, 'ID': 5978042, 'isZombie': '否', 'registerTime': 2003, 'registerMoney': '6490', 'controlType': '自然人', 'area': '湖北', 'companyType': '合伙企业' },
                5978081:{ '专利': 1, '商标': 0, '著作权': 1, 'ID': 5978081, 'isZombie': '否', 'registerTime': 2010, 'registerMoney': '7080', 'controlType': '自然人', 'area': '福建', 'companyType': '有限责任公司' },
                5978099:{ '专利': 0, '商标': 0, '著作权': 0, 'ID': 5978099, 'isZombie': '否', 'registerTime': 2012, 'registerMoney': '5120', 'controlType': '企业法人', 'area': '广东', 'companyType': '有限责任公司' },
                5988104:{ '专利': 0, '商标': 0, '著作权': 0, 'ID': 5988104, 'isZombie': '否', 'registerTime': 2004, 'registerMoney': '1560', 'controlType': '企业法人', 'area': '湖北', 'companyType': '有限责任公司' },
            },
            clusterData: {
                1500001 : [[0.759936092486962, 2.037291155884674, 1.017753063736564]],
                1500321 : [[1.121367608588425, 2.917750345951373, 4.0700835562248034]],
                1507545 : [[-0.522696158553694, 1.642302705302808, 2.560301031451777]],
                2932443 : [[1.234976405654087, 2.869887623314964, 3.786619479703405]],
                3356449 : [[1.5838132652911212, 2.696222833709265, 3.471775057831208]],
                5978041 : [[-0.8599112277305371, -0.531029538761027, -0.8090428634355591]],
                5978042 : [[-0.89509792144136, -0.447662846398486, -0.7493425804034141]],
                5978081 : [[-0.19591562696238202, 0.49817200966122405, -0.436953066454408]],
                5978099 : [[-0.8600549603005091, -0.7797176888193461, -0.37856730219274104]],
                5988104 : [[-1.78789315091665, -0.034551929830634, -4.066851820919378]],
            },
            barData: {
                1500001 : [0.0, 0.0, 0.0, 168336.0, 103540.0, 0.0, 120240.0, 977.0, -220440.0, 5050.08, 0.0, 20.04, 33400.0, 0.48, 15030.0, 1.0],
                1500321 : [0.0, 0.0, 0.0, 265905.0, 74640.0, 0.0, 961363.2, 116.0, -279900.0, 0.0, 0.0, 43261.344000000005, 522480.0, 0.47, 240340.8, 1.0],
                1507545 : [0.0, 0.0, 0.0, 141926.4, 3840.0, 0.0, 129024.0, 943.0, -31031.2482, 0.0, 0.0, 345.6, 115200.0, 0.94, 16128.0, 1.0],
                2932443 : [0.0, 0.0, 0.0, 47840.0, -36800.0, 0.0, 6900.0, 940.0, 4600.0, 1076.4, 0.0, 11.04, 23000.0, 1.8, 1380.0, 1.0],
                3356449 : [0.0, 0.0, 0.0, 355656.0, 8760.0, 420.48, 75686.4, 483.0, 8760.0, 16004.52, 420.48, 420.48, 52560.0, 0.97, 9460.8, 1.0],
                5978041 : [110880.0, 47040.0, 114800.0, 194040.0, 59500.0, 0.0, 114800.0, 873.0, -36750.0, 0.0, 0.0, 42.0, 70000.0, 0.48, 28700.0, 0.0],
                5978042 : [273358.8, 47247.2, 99686.4, 273358.8, -240130.0, 0.0, 249216.0, 110.0, 6490.0, 0.0, 2492.16, 2492.16, 311520.0, 1.95, 49843.2, 0.0],
                5978081 : [84960.0, 0.0, 33984.0, 339840.0, 7080.0, 0.0, 67968.0, 937.0, -38940.0, 0.0, 0.0, 1529.28, 35400.0, 0.96, 8496.0, 0.0],
                5978099 : [95846.4, 67584.0, 117964.8, 95846.4, -12800.0, 0.0, 147456.0, 593.0, 5120.0, 2875.3920000000003, 0.0, 943.7184, 61440.0, 1.31, 29491.2, 0.0],
                5988104 : [146764.8, 4867.2, 41184.0, 293529.6, -35100.0, 60.84, 164736.0, 788.0, -7800.0, 0.0, 549.12, 549.12, 68640.0, 1.47, 20592.0, 0.0],
            },
        }
    },
    mounted() {
        //this.initDatas()
        this.initCharts()
    },
    methods: {
        /*
        initDatas() {
            // --------------------------------------------公司信息-------------------------
            // 僵尸企业
            this.companyInfo[1500001] = { 'ID': 1500001, 'isZombie': '是', 'registerTime': 2010, 'registerMoney': '6680', 'controlType': '自然人', 'area': '山东', 'companyType': '股份有限公司' }
            this.companyInfo[1500321] = { 'ID': 1500321, 'isZombie': '是', 'registerTime': 2001, 'registerMoney': '9330', 'controlType': '企业法人', 'area': '广东', 'companyType': '股份有限公司' }
            this.companyInfo[1507545] = { 'ID': 1507545, 'isZombie': '是', 'registerTime': 2000, 'registerMoney': '3840', 'controlType': '企业法人', 'area': '山东', 'companyType': '有限责任公司' }
            this.companyInfo[2932443] = { 'ID': 2932443, 'isZombie': '是', 'registerTime': 2014, 'registerMoney': '4600', 'controlType': '企业法人', 'area': '广西', 'companyType': '集体所有制企业' }
            this.companyInfo[3356449] = { 'ID': 3356449, 'isZombie': '是', 'registerTime': 2009, 'registerMoney': '8760', 'controlType': '企业法人', 'area': '湖南', 'companyType': '农民专业合作社' }
            // 非僵尸企业
            this.companyInfo[5978041] = { 'ID': 5978041, 'isZombie': '否', 'registerTime': 2005, 'registerMoney': '3500', 'controlType': '企业法人', 'area': '山东', 'companyType': '有限责任公司' }
            this.companyInfo[5978042] = { 'ID': 5978042, 'isZombie': '否', 'registerTime': 2003, 'registerMoney': '6490', 'controlType': '自然人', 'area': '湖北', 'companyType': '合伙企业' }
            this.companyInfo[5978081] = { 'ID': 5978081, 'isZombie': '否', 'registerTime': 2010, 'registerMoney': '7080', 'controlType': '自然人', 'area': '福建', 'companyType': '有限责任公司' }
            this.companyInfo[5978099] = { 'ID': 5978099, 'isZombie': '否', 'registerTime': 2012, 'registerMoney': '5120', 'controlType': '企业法人', 'area': '广东', 'companyType': '有限责任公司' }
            this.companyInfo[5988104] = { 'ID': 5988104, 'isZombie': '否', 'registerTime': 2004, 'registerMoney': '1560', 'controlType': '企业法人', 'area': '湖北', 'companyType': '有限责任公司' }

            // --------------------------------------------聚类信息---------------------------
            this.clusterData[1500001] = [[0.759936092486962, 2.037291155884674, 1.017753063736564]];
            this.clusterData[1500321] = [[1.121367608588425, 2.917750345951373, 4.0700835562248034]];
            this.clusterData[1507545] = [[-0.522696158553694, 1.642302705302808, 2.560301031451777]];
            this.clusterData[2932443] = [[1.234976405654087, 2.869887623314964, 3.786619479703405]];
            this.clusterData[3356449] = [[1.5838132652911212, 2.696222833709265, 3.471775057831208]];

            this.clusterData[5978041] = [[-0.8599112277305371, -0.531029538761027, -0.8090428634355591]];
            this.clusterData[5978042] = [[-0.89509792144136, -0.447662846398486, -0.7493425804034141]];
            this.clusterData[5978081] = [[-0.19591562696238202, 0.49817200966122405, -0.436953066454408]];
            this.clusterData[5978099] = [[-0.8600549603005091, -0.7797176888193461, -0.37856730219274104]]
            this.clusterData[5988104] = [[-1.78789315091665, -0.034551929830634, -4.066851820919378]]

            // ------------------------------------------柱状图信息---------------------------------
            // 僵尸企业
            this.barData[1500001] = [0.0, 0.0, 0.0, 168336.0, 103540.0, 0.0, 120240.0, 977.0, -220440.0, 5050.08, 0.0, 20.04, 33400.0, 0.48, 15030.0, 1.0];
            this.barData[1500321] = [0.0, 0.0, 0.0, 265905.0, 74640.0, 0.0, 961363.2, 116.0, -279900.0, 0.0, 0.0, 43261.344000000005, 522480.0, 0.47, 240340.8, 1.0]
            this.barData[1507545] = [0.0, 0.0, 0.0, 141926.4, 3840.0, 0.0, 129024.0, 943.0, -31031.2482, 0.0, 0.0, 345.6, 115200.0, 0.94, 16128.0, 1.0]
            this.barData[2932443] = [0.0, 0.0, 0.0, 47840.0, -36800.0, 0.0, 6900.0, 940.0, 4600.0, 1076.4, 0.0, 11.04, 23000.0, 1.8, 1380.0, 1.0]
            this.barData[3356449] = [0.0, 0.0, 0.0, 355656.0, 8760.0, 420.48, 75686.4, 483.0, 8760.0, 16004.52, 420.48, 420.48, 52560.0, 0.97, 9460.8, 1.0]
            // 非僵尸企业
            this.barData[5978041] = [110880.0, 47040.0, 114800.0, 194040.0, 59500.0, 0.0, 114800.0, 873.0, -36750.0, 0.0, 0.0, 42.0, 70000.0, 0.48, 28700.0, 0.0]
            this.barData[5978042] = [273358.8, 47247.2, 99686.4, 273358.8, -240130.0, 0.0, 249216.0, 110.0, 6490.0, 0.0, 2492.16, 2492.16, 311520.0, 1.95, 49843.2, 0.0]
            this.barData[5978081] = [84960.0, 0.0, 33984.0, 339840.0, 7080.0, 0.0, 67968.0, 937.0, -38940.0, 0.0, 0.0, 1529.28, 35400.0, 0.96, 8496.0, 0.0]
            this.barData[5978099] = [95846.4, 67584.0, 117964.8, 95846.4, -12800.0, 0.0, 147456.0, 593.0, 5120.0, 2875.3920000000003, 0.0, 943.7184, 61440.0, 1.31, 29491.2, 0.0]
            this.barData[5988104] = [146764.8, 4867.2, 41184.0, 293529.6, -35100.0, 60.84, 164736.0, 788.0, -7800.0, 0.0, 549.12, 549.12, 68640.0, 1.47, 20592.0, 0.0]

        },
        */
        initCharts() {
            var myChart1 = this.$echarts.init(document.getElementById('demo1'), 'light');
            var option1 = {
                tooltip: {},
                legend: {
                    data: ["当前企业"],
                
                },
                radar: {
                    center: ['50 %', '60 %'],
                    name: {
                        textStyle: {
                        fontSize: 12,
                        // fontWeight: 'bold'
                        }
                    },
                    indicator: [{
                        text: '专利',
                        max: 2,
                        min: -0.5
                    },
                    {
                        name: '商标',
                        max: 2,
                        min: -0.5

                    },
                    {
                        name: '著作权',
                        max: 2,
                        min: -0.5

                    },
                    ]
                },
                series: [{
                type: 'radar',
                // areaStyle: {normal: {}},
                data: [{
                    value: [this.companyInfo[this.currentID]['专利'], this.companyInfo[this.currentID]['商标'], this.companyInfo[this.currentID]['著作权']],
                    // value: [0, 0, 1],
                    name: '当前企业',
                    areaStyle: {
                    },
                },
                ]
                }]
            };
            myChart1.setOption(option1);

            var myChart3 = this.$echarts.init(document.getElementById('demo3'), 'light');
            var color = ["#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c", "#9287e7"];
            var option3 = {
                color: color,
                legend: {
                    data: ['验证集僵尸平均', '验证集非僵尸平均', '训练集僵尸平均', '当前企业'],
                },
                brush: {
                    toolbox: ['rect'],
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
                    left: '5%',
                    right: '3%'
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
                data: this.barData[this.currentID],
                color: color[4],
                },
                ]
            };
            myChart3.setOption(option3);
            
            Axios.get("http://cdn.zomboost.dcts.top/prediction.json").then((res)=>{
                var myChart4 = this.$echarts.init(document.getElementById('demo4'), "light");
                var option4 = {
                    color: ["#ff7c7c", "#5bc49f", "#feb64d", "#9287e7"],
                    tooltip: {
                        trigger: "item",
                    },
                    grid3D: {
                        top: 'top'
                    },
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
                        top: 0
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
                        data: this.clusterData[this.currentID],
                        itemStyle: {
                            color: '#282c34'
                        }
                    }
                    ]
                };
                myChart4.setOption(option4);
            });
        },
        searchID(ID) {
            //console.log(ID)
            if(this.companyInfo.hasOwnProperty(ID)){
                //console.log(this.companyInfo[ID])
                this.$Message.success({
                    content: '切换企业ID为：'+ID,
                    duration: 3
                })
                this.currentID = ID
                this.initCharts()
            }else{
                this.$Message.error({
                    content: '查询失败，ID:'+ID+'不存在！',
                    duration: 3
                })
            }
        }
    }
}
</script>