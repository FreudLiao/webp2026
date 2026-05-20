import { useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";

function App() {

  // 原始資料
  const [allData, setAllData] = useState([]);

  // 搜尋後資料
  const [filteredData, setFilteredData] = useState([]);

  // 搜尋文字
  const [keyword, setKeyword] = useState("");

  // API網址
  const openUrl =
    "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6";

  // useEffect：進入頁面時呼叫 API
  useEffect(() => {
    fetch(openUrl)
      .then((res) => res.json())
      .then((data) => {

        // DataGrid 必須有 id
        const newData = data.map((item, index) => ({
          id: index,
          title: item.title,
          location:
            item.showInfo && item.showInfo.length > 0
              ? item.showInfo[0].location
              : "",
          price:
            item.showInfo && item.showInfo.length > 0
              ? item.showInfo[0].price
              : "",
        }));

        setAllData(newData);
        setFilteredData(newData);
      });
  }, []);

  // 搜尋功能
  useEffect(() => {
    const result = allData.filter((item) =>
      item.title.includes(keyword)
    );

    setFilteredData(result);
  }, [keyword, allData]);

  // DataGrid 欄位設定
  const columns = [
    { field: "title", headerName: "名稱", flex: 1 },
    { field: "location", headerName: "地點", flex: 1 },
    { field: "price", headerName: "票價", flex: 1 },
  ];

  return (
    <Box sx={{ height: 600, width: "100%", padding: 2 }}>

      <h1>景點觀光展覽資訊</h1>

      <TextField
        label="搜尋名稱"
        variant="outlined"
        fullWidth
        sx={{ marginBottom: 2 }}
        onChange={(e) => setKeyword(e.target.value)}
      />

      <DataGrid
        rows={filteredData}
        columns={columns}
        pageSizeOptions={[10]}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 10,
            },
          },
        }}
      />
    </Box>
  );
}

export default App;