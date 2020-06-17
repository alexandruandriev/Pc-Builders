import React from 'react';
import Article from '../components/Article';
import CostumForm from '../components/Form'
import axios from 'axios'

class ArticleList extends React.Component {
     state  = { 
        articles:[]  
     }
     componentDidMount(){
         axios.get('http://127.0.0.1:8000/api/').then(res =>{
             this.setState({
                articles: res.data
             });
             console.log(res.data);
         })
        

        }
    render(){
        return(
           <div>
           <Article data={this.state.articles}/>
           <h2>Create article </h2>
           <br/>
           <CostumForm
           requestType = 'post'
           articleID ={null}
           btnText = "Update"/>
           </div>
        );
    }
}
export default ArticleList;