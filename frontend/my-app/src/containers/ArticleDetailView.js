import React from 'react';
import Article from '../components/Article';
import CostumForm from '../components/Form';
import axios from 'axios';
import {Card} from 'antd';
class ArticleDetail extends React.Component {
     state  = { 
        article:{} 
     }
     componentDidMount(){
         const articleid = this.props.match.params.articleID;
         axios.get(`http://127.0.0.1:8000/api/${articleid}/`).then(res =>{
             this.setState({
                article: res.data
             });
             console.log(res.data);
         })
        

        }
    render(){
        return(
           <div>
           <Card title ={this.state.article.title}>
               <p>{this.state.article.content}</p>
           </Card>
           <CostumForm requestType="put" articleid = {this.props.match.params.articleid} btnText = "Create">
               
           </CostumForm>
           </div>
        );
    }
}
export default ArticleDetail;