-- Copy this file to /usr/lib/lua/luci/statistics/rrdtool/definitions/exec.lua
-- See lua-app-statistics source for more details on the format:
--   https://luci.subsignal.org/trac/browser/luci/tags/0.11.1/applications/luci-statistics/luasrc/statistics/rrdtool/definitions
module("luci.statistics.rrdtool.definitions.exec", package.seeall)

function rrdargs(graph, plugin, plugin_instance)
    return {
    	-- Create a chart per unique measurement instance.
        per_instance = true,
        -- Put the host and instance name in the chart title.
        title = "%H: %pi",
        -- Use a generic label on the vertical axis.
        vlabel = "Value",
        -- Define the data type of the chart.
        data = {
            types = { "gauge" },
            options = {
                gauge = {
                	-- Use a generic label for the value label.
                    title = "Value"
                }
            }
        }
    }
end