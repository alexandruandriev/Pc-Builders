import React, { useState } from 'react';
import { Form, Input, Button} from 'antd';
import axios from 'axios';
const FormItem = Form.Item;
class CostumForm extends React.Component {

  handleFormSubmit = (values,requestType,articleID) => {
    
    const title = values.title;
    const content = values.content;

    switch(requestType){
      case 'post':
          axios.post("http://127.0.0.1:8000/api/",{
            title: title,
            content: content,
          }).then(res  => console.log(res)).catch(error => console.err(error))
          break;
      case 'put':
          axios.put(`http://127.0.0.1:8000/api/${articleID}`,{
            title: title,
            content: content,
          })
          .then(res  => console.log(res))
          .catch(error => console.err(error));
          break;

    }

  }
  render(){
  return (
    <div>
      <Form onFinish={(values) => this.handleFormSubmit(
        values,
        this.props.requestType,
        this.props.articleID )}>
        <FormItem name="title" label="Title" >
          <Input placeholder="Put a title here" />
        </FormItem>
        <FormItem name ="content" label="Content" >
          <Input placeholder="Enter some content" />
        </FormItem>
        <FormItem >
          <Button type="primary" htmlType="submit">{this.props.btnText}</Button>
        </FormItem>
      </Form>
    </div>
  );
}
};
export default CostumForm;
