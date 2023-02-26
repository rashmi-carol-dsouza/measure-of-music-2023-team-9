import { useState, useMemo, useEffect } from "react";
import SearchForm, { Option } from "./SearchForm";
import Table from "./Table";
import axios from "axios";

import { genre } from './options';

console.log(genre);

type GenreProps = {
  values: string[];
};

const Genres = ({ values }: GenreProps) => {
  // Loop through the array and create a badge-like component instead of a comma-separated string
  return (
    <>
      {values.map((genreId, idx) => {
        const g = genre.find((g: Option) => g.id === genreId);
        const style = { background: g.color };
        return (
          <span key={idx} className="badge" style={style}>
            {g.name}
          </span>
        );
      })}
    </>
  );
};

type PhotoProps = {
  url: string;
};

const Photo = ({ url }: PhotoProps) => {
  return (
    <>
      <img src={url} alt="artist photo" />
    </>
  );
};

type CellProps = {
  cell: {
    value: string[];
  };
};

const Search = () => {
  const [data, setData] = useState([]);
  const [name, setName] = useState(null);

  const onSubmit = async (values: any, cb: Function) => {
    const result = await axios("https://63fa2008473885d837d8ddec.mockapi.io/collaborators");
    cb();
    setName(values.name);
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
            Header: "Photo",
            accessor: "image",
            Cell: ({ cell: { value } }: CellProps) => <Photo url={value} />,
          },
          {
            Header: "Genre(s)",
            accessor: "genres",
            Cell: ({ cell: { value } }: CellProps) => <Genres values={value} />,
          },
          {
            Header: "Compatibility Score",
            accessor: "compatibilityScore",
          },
        ],
      },
    ],
    []
  );

  return (
    <div className="search">
      <h2>Get Started</h2>
      <SearchForm handleSubmit={onSubmit} />

      {hasData && (
        <div className="results">
          <h3>
            Hey <span className="text-green">{name}</span>
          </h3>
          <p>Here are the artists we think you should collaborate with</p>
          <Table columns={columns} data={data} />
        </div>
      )}
    </div>
  );
};

export default Search;
