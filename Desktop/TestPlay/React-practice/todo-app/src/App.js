import React from "react"
import Table from "./Table"
import Form from "./Form"

class App extends React.Component{
    state = { char : []}
    handleSubmit = this.handleSubmit.bind(this)
    rmChar = this.rmChar.bind(this)
    rmChar(idx){
        this.setState({
            char: this.state.char.filter((char,i) =>{
                return i !== idx
            })
        })
    }
    handleSubmit(new_char){
        this.setState({char : [...this.state.char, new_char]})
    }
    render(){
        return(
            <div >
                <h1>Todo</h1>
                <Table charData={this.state.char} removeChar={this.rmChar}/>
                <h3>Add Task</h3>
                <Form handleSubmit={this.handleSubmit}/>

            </div>
        )
    }
}
export default App;