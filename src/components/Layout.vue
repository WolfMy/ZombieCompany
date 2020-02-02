<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo"></div>
                </Menu>
            </Header>
            <Layout>
                <Sider :style="{background: '#fff'}">
                    <Menu theme="light" width="auto" :open-names="['1']">
                        <Submenu name="1">
                            <template slot="title">
                                <Icon type="ios-navigate"></Icon>
                                系统菜单
                            </template>
                            <!--暂时取消单条查询功能
                            <router-link to="/SingleQuery" style="color:#515a6e;"><MenuItem name="1-1">单条查询</MenuItem></router-link>
                            -->
                            <router-link to="/BatchQuery" style="color:#515a6e;"><MenuItem name="1-2">批量查询</MenuItem></router-link>
                            <router-link to="/DataVisualization" style="color:#515a6e;"><MenuItem name="1-3">数据可视化</MenuItem></router-link>
                        </Submenu>
                    </Menu>
                </Sider>
                <Layout :style="{padding: '0 24px 24px'}">
                    <Content :style="{padding: '24px', minHeight: '500px', background: '#fff'}">
                        <slot />
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    </div>
</template>

<script>
    export default {
        
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