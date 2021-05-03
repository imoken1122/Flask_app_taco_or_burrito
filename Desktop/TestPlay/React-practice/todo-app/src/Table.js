import React from "react"

const TableHeader = () => {
    return(
        <thead>
            <tr>
                <th>Name</th>
                <th>Job</th>
                <th>Remove</th>
            </tr>
        </thead>
    )
}
const TableBody = props => {
    const rows = props.charData.map((row,idx) =>{
        return (
            <tr key={idx}>
                <td>{row.name}</td>
                <td>{row.job}</td>
                <td><button onClick={() => props.rmChar(idx)}>Delete</button></td>
            </tr>
        )}
    )
    return <tbody>{rows}</tbody>
}
const Table = props =>{

    return (
        <table>
            <TableHeader />
            <TableBody charData={props.charData} rmChar={props.removeChar}/>
        </table>
    )
}
export default Table;