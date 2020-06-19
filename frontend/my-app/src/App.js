import React,{ Component } from 'react';


import './App.css';
import 'antd/dist/antd.css';
import { BrowserRouter as Router} from 'react-router-dom';
import CostumLayout from './containers/Layout';
import ArticleList from './containers/ArticleListView'
import Article from './components/Article';
import BaseRouter from './routes'




class App extends Component {
 render(){
    return(
       <div className = "App">
          <Router>

          
          <CostumLayout>
              <BaseRouter/>
              
          </CostumLayout>
          </Router>
          
       </div>
    );



 }
}
export default App;
