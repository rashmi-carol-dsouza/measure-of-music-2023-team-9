import { useState, useMemo, useEffect } from "react";
import SearchForm from "./SearchForm";
import Table from "./Table";
import axios from "axios";


type GenreProps = {
  values: string[]
}

const Genres = ({ values }: GenreProps) => {
  // Loop through the array and create a badge-like component instead of a comma-separated string
  return (
    <>
      {values.map((genre, idx) => {
        return (
          <span key={idx} className="badge">
            {genre}
          </span>
        );
      })}
    </>
  );
};

type CellProps = {
  cell: {
    value: string[]
  }
}

const Search = () => {
  const [data, setData] = useState([]);

  const onSubmit = async () => {
    const result = await axios("https://63fa2008473885d837d8ddec.mockapi.io/collaborators");
    setData(result.data);
  };

  const hasData = data.length > 0;

  /* 
    - Columns is a simple array right now, but it will contain some logic later on. It is recommended by react-table to memoize the columns data
    - Here in this example, we have grouped our columns into two headers. react-table is flexible enough to create grouped table headers
  */

  const columns = useMemo(
    () => [
      {
        // first group - Matching Artists
        Header: "Matching Artists",
        // First group columns
        columns: [
          {
            Header: "Name",
            accessor: "name",
          },
        ],
      },
      {
        // Second group - Details
        Header: "Details",
        // Second group columns
        columns: [
          {
            Header: "Genre(s)",
            accessor: "genres",
            Cell: ({ cell: { value } }: CellProps) => <Genres values={value} />,
          },
          {
            Header: "Energy",
            accessor: "energy",
          },
          {
            Header: "Past Collaborations",
            accessor: "pastCollabs",
          },
        ],
      },
    ],
    []
  );

  return (
    <div className="search">
      <h2>Get Started</h2>
      <SearchForm handleSubmit={onSubmit}/>

      {hasData && (
        <div className="results">
          <h3>
            Best Collabs for <span className="text-green">PinkPanthress</span>
          </h3>
          <Table columns={columns} data={data} />
        </div>
      )}
    </div>
  );
};

export default Search;
