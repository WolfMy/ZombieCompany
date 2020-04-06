<template>
    <div class="layout">
        <Layout>
            <Header>
                <img class="layout-logo" src="logo.png">
                <!--p class="layout-logo-text">ZomBoost</p-->
                <!--p style="color:#fff;position:fixed;left:7%;font-size=32px;">僵尸企业智能预测</p-->
                <Menu v-show="isShow" class="layout-menu" theme="dark" mode="horizontal" style="text-align:left;">
                    <MenuItem name="0" to="/Home">
                        <Icon type="ios-home" />
                            首页
                    </MenuItem>
                    <MenuItem name="1-1"  to="/BatchQuery">
                        <Icon type="ios-ionitron" />
                        僵尸企业智能预测
                    </MenuItem>
                    <Submenu name="DataVisualization">
                        <template slot="title">
                            <Icon type="ios-podium" />
                            数据可视化展示
                        </template>
                        <MenuItem name="2-1" to="/DataVisualization/BasicInformation">
                            <Icon type="ios-pie" />
                            数据分布可视化
                        </MenuItem>
                        <MenuItem name="2-2" to="/DataVisualization/RelevanceExplore">
                            <Icon type="ios-analytics" />
                            数据关联性探索
                        </MenuItem>
                        <MenuItem name="2-3" to="/DataVisualization/CorporatePortraits">
                            <Icon type="ios-reverse-camera" />
                            僵尸企业画像
                        </MenuItem>
                        <MenuItem name="2-4" to="/DataVisualization/ModelTraining">
                            <Icon type="ios-flask" />
                            模型训练可视化
                        </MenuItem>
                    </Submenu>
                </Menu>
            </Header>
            <Layout>
                <div v-show="!isShow" style="position:fixed;top:50%;margin:-25px;">
                <ButtonGroup vertical>
                    <Button @click="isCollapsed = true" shape="circle" style="background:#515a6e;height:100px;width:40px;text-align:left;">
                        <Icon type="ios-arrow-forward" color="white" size="32" />
                    </Button>
                </ButtonGroup>
                <Drawer title="僵尸企业检测" placement="left" :closable="false" v-model="isCollapsed" >
                    <Menu theme="light" mode="vertical" width="auto" @on-select="isCollapsed = false">
                        <MenuItem name="0" to="/Home">
                            <Icon type="ios-home" />
                                首页
                        </MenuItem>
                        <MenuGroup title="系统菜单">
                            <MenuItem name="1-1"  to="/BatchQuery">
                                <Icon type="ios-ionitron" />
                                僵尸企业智能预测
                            </MenuItem>
                        </MenuGroup>
                        <MenuGroup title="数据可视化展示">
                            <MenuItem name="2-1" to="/DataVisualization/BasicInformation">
                                <Icon type="ios-pie" />
                                数据分布可视化
                            </MenuItem>
                            <MenuItem name="2-2" to="/DataVisualization/RelevanceExplore">
                                <Icon type="ios-analytics" />
                                数据关联性探索
                            </MenuItem>
                            <MenuItem name="2-3" to="/DataVisualization/CorporatePortraits">
                                <Icon type="ios-reverse-camera" />
                                僵尸企业画像
                            </MenuItem>
                            <MenuItem name="2-4" to="/DataVisualization/ModelTraining">
                                <Icon type="ios-flask" />
                                模型训练可视化
                            </MenuItem>
                        </MenuGroup>
                    </Menu>   
                </Drawer>
                </div>
                <Layout :style="{padding: '0 24px 24px'}">
                    <Content :style="{padding: '12px 0px', minHeight: '700px', background: '#f5f7f9'}">
                        <slot />
                    </Content>
                    <Footer style="text-align:center;">2019-2020 Created By 讨论404</Footer>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isShow: true,
                isCollapsed: false
            }
        },
        mounted() {
            // 适配手机端，隐藏菜单栏
            let w = document.documentElement.offsetWidth || document.body.offsetWidth;
            if(w < 576){
                this.isShow = false;
            }
        }
    }
</script>

<style scoped>
.layout{
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 33px;
    height: 33px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-logo-text {
    font-family: Verdana;
    color: #ffffff;
    float: left;
    position: relative;
    left: 25px;
}
.layout-menu{
    float: right;
    position: relative;
    top: 0px;
    right: 20px;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
</style>