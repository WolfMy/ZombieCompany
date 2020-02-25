<template>
<div class="home">
    <Row>
        <Col span="24">
            <Card dis-hover style="margin:24px 0px;padding:24px 24px;">
                <h1>讨论404</h1>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
                <p class="lead text-muted">描述:....<strong>强调词</strong>...</p>
            </Card>
        </Col>
    </Row>
    <Row :gutter="16">
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/BatchQuery.png" slot="title" class="card-img-top">
                <h5>僵尸企业批量检测</h5>
                <p>描述:.....</p>
                <p>描述:.....</p>
                <p>描述:.....</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/BasicInformation.png" slot="title" class="card-img-top">
                <h5>基本信息</h5>
                <p>描述:.....</p>
                <p>描述:.....</p>
                <p>描述:.....</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/RelevanceExplore.png" slot="title" class="card-img-top">
                <h5>关联性探究</h5>
                <p>描述:.....</p>
                <p>描述:.....</p>
                <p>描述:.....</p>
            </Card>
        </Col>
        <Col :xs="24" :md="6" style="margin:0px 0px 16px 0px;">
            <Card style="text-align:left;">
                <img src="home/CorporatePortraits.png" slot="title" class="card-img-top">
                <h5>僵尸企业画像</h5>
                <p>描述:.....</p>
                <p>描述:.....</p>
                <p>描述:.....</p>
            </Card>
        </Col>
    </Row>
    
</div>
</template>
<script>
export default {
    mounted(){
        
    }
}
</script>
<style scoped>
h1 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem!important;
    color: #464c5b;
}
p {
    color: #657180;
}
.lead {
    margin-top: 0;
    margin-bottom: 1rem;
    font-size: 1.25rem;
    font-weight: 300;
}
.card-img-top {
    width: 100%;
    border-top-left-radius: calc(.25rem - 1px);
    border-top-right-radius: calc(.25rem - 1px);
}
</style>