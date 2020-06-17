import React,{ Component } from 'react';


import './App.css';
import 'antd/dist/antd.css';
import CostumLayout from './containers/Layout';
import ArticleList from './containers/ArticleListView'
import Article from './components/Article';




class App extends Component {
 render(){
    return(
       <div className = "App">
          <CostumLayout>
              <ArticleList/>
              <ArticleList/>
          </CostumLayout>
       </div>
    );



 }
}
export default App;
