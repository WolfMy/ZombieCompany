<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo"></div>
                </Menu>
            </Header>
            <Layout>
                <ButtonGroup style="position:fixed;top:50%;margin:-25px" vertical>
                    <Button @click="isCollapsed = true" shape="circle" style="background:#515a6e;height:100px;width:50px;text-align:left;">
                        <Icon type="ios-arrow-forward" color="white" size="40" />
                    </Button>
                </ButtonGroup>
                <Drawer title="僵尸企业检测" placement="left" :closable="false" v-model="isCollapsed" >
                    <Menu theme="light" mode="vertical" width="auto" @on-select="isCollapsed = false">
                        <MenuGroup title="系统菜单">
                            <MenuItem name="1-1"  to="/BatchQuery">
                                <Icon type="ios-search" />
                                批量查询
                            </MenuItem>
                        </MenuGroup>
                        <MenuGroup title="数据可视化">
                            <MenuItem name="2-1" to="/DataVisualization/BasicInformation">
                                <Icon type="ios-information-circle-outline" />
                                基本信息
                            </MenuItem>
                            <MenuItem name="2-2" to="/DataVisualization/RelevanceExplore">
                                <Icon type="ios-analytics" />
                                关联性探索
                            </MenuItem>
                            <MenuItem name="2-3" to="/DataVisualization/CorporatePortraits">
                                <Icon type="ios-reverse-camera" />
                                僵尸企业画像
                            </MenuItem>
                        </MenuGroup>
                    </Menu>   
                </Drawer>
                <Layout :style="{padding: '0 24px 24px'}">
                    <Content :style="{padding: '12px', minHeight: '500px', background: '#f5f7f9'}">
                        <slot />
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isCollapsed: false
            }
        },
        methods:{
        }
    }
</script>

<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
</style>